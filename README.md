# Documentatie
Dit is de documentatie van het Fun Fun Lighting and Sound System. Hierin wordt beschreven hoe het systeem werkt en hoe het is opgebouwd.

## Aanpassingen
Om aanpassingen te doen aan de EventLoop open je dit bestand:

- `Raspberry-Pi-1b/eventLoop.py`

## Verantwoordelijkheden
Het systeem bevat 2 onderdelen die beiden verantwoordelijk zijn voor twee verschillende dingen. Deze verdeling zie je ook in de mappen.
2. De Raspberry Pi 1b
1. De Raspberry Pi Pico

### Raspberry Pi Pico
De Raspberry Pi Pico is verantwoordelijk voor het aansturen van de LED strip. Dit doet hij door middel van een PWM signaal via de GPIO pinnen. De Pico ontvangt commando's van de Raspberry Pi 1b via een seriële verbinding.

### Raspberry Pi 1b
De Raspberry Pi 1b is verantwoordelijk voor het ontvangen van commando's van de gebruiker en deze door te sturen naar de Raspberry Pi Pico. Dit doet hij door middel van een seriële verbinding. Deze commando's worden gestuurd op basis van een timeline die de gebruiker kan maken.

De RPI 1b is ook verantwoordelijk voor de muziek die afgespeeld wordt. De muziek wordt afgespeeld via een 3.5mm jack aansluiting.

## Protocol
Het protocol dat gebruikt wordt om commando's te sturen van de Raspberry Pi 1b naar de Raspberry Pi Pico is een simpel protocol. Het protocol werkt als volgt:
`{LEDKAST}-{DMX EFFECT}-{RGB COLOR}`

Een voorbeeld is:
`LEDKAST_1 TWINKLE rgb(255, 0, 0)`

## Beschikbare effecten
Er zijn verschillende effecten beschikbaar die de gebruiker kan kiezen. De effecten zijn:
1. STATIC
2. RAINBOW
3. RAINBOW_CYCLE
4. THEATER_CHASE
5. THEATER_CHASE_RAINBOW
6. COLOR_WIPE
7. SCANNER
8. FADE
9. TWINKLE
10. FLASH
11. CLEAR


# Hardware
## Verbinden
Om te verbinden met de Hoofdkast log je in op het FunFun Verlichting netwerk. Het wachtwoord is `12345678`, vervolgens kun je via ssh verbinden met de Raspberry Pi 1b.

## VNC
VNC viewer is uitgeschakeld op de Raspberry Pi 1b vanwege performance redenen. Als je toch VNC wilt gebruiken kun je dit inschakelen door het volgende commando uit te voeren:
`sudo raspi-config`

## Knoppen
Er zijn vier knoppen aanwezig op de Raspberry Pi 1b. Deze knoppen hebben de volgende functionaliteiten:
1. Previous/Vorige knop: Starten van main script
2. Play/Pauze knop: Niks
3. Next/Volgende knop: Starten van pauze script
4. Mode knop: Niks