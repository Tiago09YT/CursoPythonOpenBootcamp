import time
tiempo = time.gmtime()
if(tiempo.tm_hour >=19):
    print("ve a casa")
elif(tiempo.tm_hour == 18):
    tiempoRestanteMin = 60 - tiempo.tm_min
    print("Te quedan "+ str(tiempoRestanteMin) + ' minutos.')
elif(tiempo.tm_min == 0):
    tiempoRestante2= 19 - tiempo.tm_hour
    print("Te quedan "+ str(tiempoRestante2) + ' horas.')
else:
    horasRestantes = 18 - tiempo.tm_hour
    minutosRestantes = 60 - tiempo.tm_min
    print("Te quedan "+ str(horasRestantes) + ' horas y '+ str(minutosRestantes) + " minutos.")
