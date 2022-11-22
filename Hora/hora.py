
import time

hora = time.strftime('%H')
minutos = time.strftime('%M')

if int(hora) >= 1500:
    print("Es hora de irse a casa")
else:
    print("Quedan {} horas y {} minutos para irnos a casa".format(14 - int(hora), 59-int(minutos)))
