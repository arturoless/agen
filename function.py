import random
import math
import numpy as np
import matplotlib.pyplot as plt

import individual

def conv_binario(dec):
    decode = []
    final = ''
    if dec == 0:
        decode.insert(0, '0')
    else:
        while dec != 0:
            if int(dec) % 2 != 0:
                decode.insert(0, '1')
            else:
                decode.insert(0, '0')
            dec = int(dec/2)
    while len(decode) != 16:
        decode.insert(0, '0')
    for n in decode:
        final += n
    return final


poblacion = []
for _ in range(16):
    value = conv_binario(random.randint(1, 59999)) + \
        conv_binario(random.randint(1, 59999))
    poblacion.append(individual.Individuo(value, individual.fitness(value), 0))

poblacion = sorted(poblacion, key=lambda x: x.fitness)

a = int(poblacion[0].value[0:16], 2)/10000
b = int(poblacion[0].value[16::], 2)/10000
valores_y_individuo = []
sumatoria = 0
for i in range(len(individual.valores_x)):
    y_individuo = math.cos(a*individual.valores_x[i])*math.sin(b*individual.valores_x[i])
    valores_y_individuo.append(y_individuo)
    sumatoria += (abs(individual.valores_y[i]-y_individuo))
print(valores_y_individuo)


def dibujar(x, y, ya):
    plt.plot(x, color="b")
    plt.plot(y, color="red")
    plt.plot(ya, color="black")
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.show()

if __name__ == "__main__":
    individual.cruza(poblacion)
    dibujar(individual.valores_x, individual.valores_y, valores_y_individuo)
    print('end')