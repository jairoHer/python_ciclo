#nohup python3 ciclo.py &
import time

numero = 0
while (True):
    print("iteracion:"+str(numero))
    time.sleep(1)
    numero +=1