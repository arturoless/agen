import random
import math

probabilidad_mutar_por_bit = 1/2

valores_x = [
    0.0000,
    0.2500,
    0.5000,
    0.7500,
    1.0000,
    1.2500,
    1.5000,
    1.7500,
    2.0000,
    2.2500,
    2.5000,
    2.7500,
    3.0000,
    3.2500,
    3.5000,
    3.7500,
    4.0000,
    4.2500,
    4.5000,
    4.7500,
    5.0000]
valores_y = [
    0.0718,
    0.7662,
    0.1141,
    0.4308,
    1.0211,
    0.0990,
    -0.1259,
    0.3917,
    -0.4505,
    -0.7924,
    0.0488,
    -0.2854,
    -0.5207,
    0.5606,
    0.5358,
    0.0468,
    0.8422,
    0.7356,
    -0.2180,
    0.1824,
    0.1724]


class Individuo:
    def __init__(self, value, fitness, probability):
        self.value = value
        self.fitness = fitness
        self.probability = probability

    def __repr__(self):
        return '{'+str(self.value)+','+str(self.fitness)+','+str(self.probability)+'}'


def mutar(individuo):
    array_individuo = list(individuo)
    index = 0
    for bit in array_individuo:
        azar_mutar = random.random()
        if azar_mutar <= probabilidad_mutar_por_bit:
            if bit == '1':
                array_individuo[index] = '0'
            else:
                array_individuo[index] = '1'
        index += 1
    return ''.join(array_individuo)


def fitness(value):
    a = int(value[0:16], 2)/10000
    b = int(value[16::], 2)/10000
    sumatoria = 0
    for i in range(len(valores_x)):
        y_individuo = math.cos(a*valores_x[i])*math.sin(b*valores_x[i])
        sumatoria += math.pow(abs(valores_y[i]-y_individuo), 2)
    return sumatoria/len(valores_x)
