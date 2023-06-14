import config
from binance.client import Client
import time

dias = config.dias
client = Client(config.API_KEY, config.API_SECRET, tld='com')

listTiks = []


def buscarTicks():
    ticks = []

    while True:
        try:
            list_of_tickers = client.futures_symbol_ticker()
        except Exception as e:
            print(e)
            archivo = open("log.txt", "a")
            mensaje = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime()) + ' ERROR: ' + str(e) + "\n"
            archivo.write(mensaje)
            archivo.close()
            time.sleep(2)
        else:
            break

    for tick in list_of_tickers:
        if tick['symbol'][-4:] != 'USDT':
            continue
        ticks.append(tick['symbol'])
    return ticks

def analizarMoneda(tick):
    while True:
        try:
            klines = client.futures_klines(symbol=tick, interval=client.KLINE_INTERVAL_1DAY, limit=dias)
        except Exception as e:
            print(e)
            archivo = open("log.txt", "a")
            mensaje = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime()) + ' ERROR: ' + str(e) + "\n"
            archivo.write(mensaje)
            archivo.close()
            time.sleep(2)
        else:
            break

    nKlines = len(klines)-1
    oldClose = float(klines[0][4])
    newClose = float(klines[nKlines][4])
    porcentaje = round((newClose - oldClose)/oldClose*100, 2)

    listTiks.append((tick, oldClose, newClose, porcentaje))
    #print(listTiks)
    #print("TICK: "+tick+" OLD:"+str(oldClose)+" NEW: "+str(newClose)+" PORCENTAJE: "+str(porcentaje)+"%")

def showResults():
    ordenar = sorted(listTiks, key=lambda result: result[3])
    for r in ordenar:
        print("TICK: "+r[0]+" OLD:"+str(r[1])+" NEW: "+str(r[2])+" PORCENTAJE: "+str(r[3])+"%")
