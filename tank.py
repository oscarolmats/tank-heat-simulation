A=100 #m^2, yta för tanken
Tsi=80 #°C, starttemperatur för tanken
R=1 #m^2*K/W, värmemotstånd för tanken
h=25 #konvektivt värmeöverföringstal, W/m^2*K
Ta=-20 #°C, omgivningstemperatur
m=139000 #kg, OBS! för endast 1 tank
Cp=4180 #J/kg*K, värmekapacitet för vatten
dkulvert=200 #m, kulvertens längd tur och retur
Pvärme=100000 #W, värmeuttag från tanken
Pkulvert=5*dkulvert #W, värmeförlust genom kulvert

T_current = Tsi  # Starttemperatur
E_total = 0  # Total energiförbrukning
print(f"Starttemperatur: {T_current}°C")

for timme in range(0, 13):
    # Beräkna yttemperatur baserat på nuvarande tanktemperatur
    Ts = ((A*T_current/R)+(h*A*Ta))/((h*A)+(A/R))
    
    # Beräkna värmeförlust baserat på nuvarande temperatur
    q = h*A*(Ts-Ta)+Pvärme+Pkulvert
    
    # Beräkna energi för denna timme (kWh)
    E_timme = (q/1000) * 1  # kW * 1 timme = kWh  
    E_total += E_timme
    
    # Beräkna temperaturminskning under en timme (3600 sekunder)
    temp_minskning = (q*3600)/(m*Cp)
    
    # Uppdatera temperaturen
    T_current = T_current - temp_minskning
    
    print(f"Efter {timme} timmar: {T_current:.1f}°C (effekt: {q/1000:.1f} kW, Ackumulerad energiförlust: {E_total:.1f} kWh)")

#Tar lågt pris nattetid och jämn effekt ut varandra?