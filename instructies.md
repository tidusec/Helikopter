# Recruitmentopdracht: Helikopter

**Programmeertaal**: vrij te kiezen. Als je niet weet welke te gebruiken, kies dan tussen TypeScript of Ruby.

**Opdracht**: Schrijf een programma dat een helikopter simuleert. De helikopter kan in drie richtingen bewegen en moet de volgende instructies ondersteunen:
* Keer naar rechts (R)
* Keer naar links (L)
* Ga vooruit (V)
* Ga omhoog (U)
* Ga omlaag (D)

**Opmerkingen**:
* De bewegingen vooruit/omhoog/omlaag zijn steeds één unit.
* De helikopter vliegt rond in een oneindige ruimte en moet steeds een locatie hebben (x, y, z coördinaten + richting).
* De initiële locatie van de helikopter wordt meegegeven als input in het formaat "X Y Z R", waarbij R de richting is (noord, oost, zuid, west).
* De X-as is west-oost, de Y-as noord-zuid en de Z-as de hoogte.

Je programma moet een string accepteren die overeenkomt met instructies voor de helikopter. De output van het programma is de locatie en de richting van de helikopter.

## Voorbeeld
Input: 0 0 0 noord UURVVVLVVRRVD

Dat wil zeggen:
* We beginnen op (0, 0, 0) N
* Ga omhoog, 2x (0, 0, 2) N
* Draai naar rechts (0, 0, 2) N
* Ga 3 eenheden vooruit (3, 0, 2) N
* Draai naar links (3, 0, 2) N
* Ga 2 eenheden vooruit (3, 2, 2) N
* Draai twee keer naar rechts (3, 2, 2) Z
* Ga 1 eenheid vooruit (3, 1, 2) Z
* Ga 1 eenheid omlaag (3, 1, 1) Z

De output voor deze input zou (3, 1, 1) richting het zuiden moeten zijn.

**Bonuspunten (niet verplicht)**: 
- schrijf voor de opdracht één of meerdere testen.
- zoek de fout in de oplossing

## Credits
Deze opdracht is grotendeels geïnspireerd door [Toy Robot](https://github.com/RafaelChefe/toy_robot) en de Datacamp internship 'Robot' opdracht.