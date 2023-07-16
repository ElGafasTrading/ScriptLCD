from functions import *

ticks = buscarTicks()
ticksNumber = len(ticks)
print("NUMERO DE TICKS: " + str(ticksNumber))
print("NUMERO DE DIAS A ESTIMAR: " + str(dias))

for tick in ticks:
    analizarMoneda(tick)
showResults()
