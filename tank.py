A=100
Tsi=80
R=1
h=25
Ta=-20
m=139000 #kg
Cp=4180 #J/kg*K

T_current = Tsi  # Starttemperatur
print(f"Starttemperatur: {T_current}°C")

for timme in range(0, 11):
    # Beräkna yttemperatur baserat på nuvarande tanktemperatur
    Ts = ((A*T_current/R)+(h*A*Ta))/((h*A)+(A/R))
    
    # Beräkna värmeförlust baserat på nuvarande temperatur
    q = h*A*(Ts-Ta)+100000
    
    # Beräkna temperaturminskning under en timme (3600 sekunder)
    temp_minskning = (q*3600)/(m*Cp)
    
    # Uppdatera temperaturen
    T_current = T_current - temp_minskning
    
    print(f"Efter {timme} timmar: {T_current:.1f}°C (värmeförlust: {q/1000:.1f} kW)")