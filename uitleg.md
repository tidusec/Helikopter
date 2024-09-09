# Uitleg

Elk probleem moet opgesplitst worden in sub-problemen om het mooi en elegant op te lossen.
In dit geval zullen we deze stappen moeten uitvoeren:

- Wiskundige benadering van het probleem (hoe gedragen de vectoren zich; welke bewerking moet je uitvoeren)
- Opschrijven van het programma dat dit zal doen

## Wiskundige benadering

Uit de opgave weten we dat dit gaat over een oneindige ruimte, en de makkelijkste manier om beweging voor te stellen
lijkt mij met vectoren.

We weten meteen dat los van de richting waarin je kijkt u (omhoog) en D (omlaag) voorgesteld kunnen worden
met deze vectoren omdat deze onafhankelijk zijn van de richting waarin je kijkt (helikopter kan immers 
niet naar boven kijken):

U = (0, 0, 1)

D = (0, 0 , -1)

Om deze uit te voeren moeten we simpelweg de huidige positie optellen met die vectoren.

vb: UUUD

(0, 0, 0) ->
(0, 0, 1) ->
(0, 0, 2) ->
(0, 0, 3) ->
(0, 0, 2)

---

Vervolgens is het enige wat we moeten onderzoeken het gedrag van vectoren afhankelijk van de richting waarin je kijkt.
Gezien we het probleem al opgelost hebben voor de 3D-ruimte (en de andere bewegingen onafhankelijk zijn van de Z-as), kan dit probleem nu 
vertaald worden naar een xy assenstelsel (cartesiaans).

Stel je kijkt naar het noorden vanuit de oorsprong naar het noorden is dat equivalent met 
kijken naar de y-as met alle positieve getallen daarop ge-ijkt (uiteraard figuratieve uitleg om wat ik zie conceptueel uit
te leggen). Vervolgens is het triviaal als ik een keer naar voren ga dat ik zo beweeg (dit zijn xy coördinaten):
(0, 0) →
(0, 1)

Maar de grote vraag die nu meteen duidelijk zal worden is wat gebeurt er indien ik naar rechts 
draai, en dan naar voren ga. Omdat dit voorbeeld nu zo simpel is, is het triviaal wat er gebeurt:
(0, 0) → (1, 0)

Hetzelfde als ik nog eens naar rechts draai dan gebeurt het volgende als ik naar voor ga:
(0, 0) → (0, -1)

En nog eens als ik naar rechts draai:
(0, 0) → (-1, 0)

Dit hebbende opgeschreven op een bladje papier heb ik meteen gezien dat wat je moet doen om een 
vector 90 graden te draaien niet zo moeilijk is:

Stel je hebt een vector (x, y) dan is die vector 90 graden met de klok mee gedraaid gelijk aan:

(y, -x)

--- 
Dit wetende is het nu triviaal om bewegingen uit te voeren. Je berekent gewoon 
op basis van de richting waarin je kijkt de resulterende bewegingsvector, en dan tel je die op bij de huidige positie.

## Programma zelf

Ik ben gewoon om eerder object gericht te programmeren, dus ik zal een 
Class maken waarin alle functies van de helikopter zitten.

## Bonuspunten

- De fout in de oplossing van het voorbeeld is dat bij de derde
instructie (Draai naar rechts) er nog steeds noord (N) staat, terwijl dat hier oost (O) moet staan
dit wordt gecompenseerd door het feit dat in instructie 5 je terug naar links gaat (dus terug richting het noorden).
Voor de rest is alles correct en mist er niets.

