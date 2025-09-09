# Tank Heat Loss Simulation

Ett Python-program som simulerar värmeförlust från en tank över tid.

## Beskrivning

Programmet beräknar hur en varm tank förlorar värme till omgivningen och visar temperaturutvecklingen timme för timme. Simulationen tar hänsyn till att värmeförlusten minskar när tankens temperatur sjunker.

## Parametrar

- **A**: Tankens ytarea (m²)
- **Tsi**: Tankens starttemperatur (°C)
- **R**: Termisk resistans
- **h**: Värmeöverföringskoefficient (W/(m²·K))
- **Ta**: Omgivningstemperatur (°C)
- **m**: Massan av vätskan (kg)
- **Cp**: Specifik värmekapacitet (J/(kg·K))

## Användning

```bash
python tank.py
```

## Output

Programmet visar:
- Starttemperatur
- Temperatur för varje timme (0-10 timmar)
- Aktuell värmeförlust för varje timme

## Fysik

Programmet använder grundläggande värmeöverföringsprinciper och uppdaterar värmeförlusten dynamiskt baserat på den aktuella temperaturen för en mer realistisk simulation. 