from functions import *

ticks = buscarTicks()
ticksNumber = len(ticks)
print("NUMERO DE TICKS: " + str(ticksNumber))

for tick in ticks:
    analizarMoneda(tick)
showResults()
