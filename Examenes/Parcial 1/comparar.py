import time
import contar_palabras_v1 as ob
import contar_palabras_v2 
import random as r

inicio = time.time()
ContarPalabrasV1 =("
            La justicia sobre la fuerza es la impotencia, la fuerza sin justicia es tiranía,
            Vale más saber alguna cosa de todo que saberlo todo de una sola cosa.
            Dos excesos: excluir la razón, no admitir más que la razón.
            Nuestra naturaleza está en movimiento. El reposo absoluto es la muerte.
            El hombre tiene ilusiones como el pájaro alas. Eso es lo que lo sostiene.
            El hombre está dispuesto siempre a negar todo aquello que no comprende.
            Aquel que duda y no investiga, se torna no sólo infeliz, sino también injusto.
            A fuerza de hablar de amor, uno llega a enamorarse.
            ¿De qué le sirve al hombre ganar el mundo si pierde su alma?)
deltaV1 = time.time()-inicio

inicio = time.time()
ContarPalabrasV2 = ("
            La justicia sobre la fuerza es la impotencia, la fuerza sin justicia es tiranía.
            Vale más saber alguna cosa de todo que saberlo todo de una sola cosa.
            Dos excesos: excluir la razón, no admitir más que la razón.
            Nuestra naturaleza está en movimiento. El reposo absoluto es la muerte.
            El hombre tiene ilusiones como el pájaro alas. Eso es lo que lo sostiene.
            El hombre está dispuesto siempre a negar todo aquello que no comprende.
            Aquel que duda y no investiga, se torna no sólo infeliz, sino también injusto.
            A fuerza de hablar de amor, uno llega a enamorarse.
            ¿De qué le sirve al hombre ganar el mundo si pierde su alma?")
deltaV2 = time.time()-inicio
print(deltaV1, deltaV2)