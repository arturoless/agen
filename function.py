import individual
import random
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')


probabilidad_mutar_por_individuo = 1/2
probabilidad_mutar_por_bit = 1/2
NUM_ITERACIONES = 10
poblacion = []
promedios=[]
mejores=[]
peores=[]

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


def promedio(poblacion):
    promedio = 0.0
    for i in range(0, len(poblacion)):
        promedio = promedio+float(poblacion[i].value)
    print(f'PROMEDIO: {promedio/len(poblacion)}')
    print(f'TAMAÑO: {len(poblacion)}')
    return promedio/len(poblacion)


for _ in range(16):
    value = conv_binario(random.randint(1, 59999)) + \
        conv_binario(random.randint(1, 59999))
    poblacion.append(individual.Individuo(value, individual.fitness(value), 0))

poblacion = sorted(poblacion, key=lambda x: x.fitness)

generation = 0

for _ in range(NUM_ITERACIONES):
        # fitness_sum = sum([ind.fitness for ind in poblacion])
        # probability_offset = 0

        # for ind in poblacion:
        #     ind.probability = probability_offset + (ind.fitness / fitness_sum)
        #     probability_offset += ind.probability

    children = []
    for padre in poblacion:
        parent_1 = padre
        parent_2 = poblacion[random.randint(0, 15)]
        # rand = random.random()
        # for ind in poblacion:
        #     if ind.probability < rand:
        #         parent_1=ind
        #         break
        # rand = random.random()
        # for ind in poblacion:
        #     if ind.probability < rand:
        #         parent_2=ind
        #         break
        indice_cruza = random.randint(0, 31)
        value1 = parent_1.value[0:indice_cruza] + \
            parent_2.value[indice_cruza:32]
        value2 = parent_2.value[0:indice_cruza] + \
            parent_1.value[indice_cruza:32]
        children.append(individual.Individuo(value1, 0, 0))
        children.append(individual.Individuo(value2, 0, 0))

    poblacion += children
    mejor_poblacion = []
    for individuo in poblacion:
        azar = random.random()
        if azar <= probabilidad_mutar_por_individuo:
            individuo.value = individual.mutar(individuo.value)
        a = int(individuo.value[0:16], 2)/10000
        b = int(individuo.value[16::], 2)/10000

        if a < 6 and b < 6:
            individuo.fitness = individual.fitness(individuo.value)
            mejor_poblacion.append(individuo)
    sorted_ind = sorted(mejor_poblacion, key=lambda x: x.fitness)

    #sacar datos
    mejores.append(sorted_ind[0].fitness)
    promedios.append(promedio(sorted_ind))
    peores.append(sorted_ind[len(sorted_ind)-1].fitness)


    poblacion = sorted_ind[0:16]
    print(f'------------------Generación: {generation}---------------------')
    print(poblacion[0])
    print(int(poblacion[0].value[0:16], 2)/10000)
    print(int(poblacion[0].value[16::], 2)/10000)
    generation += 1
a = int(poblacion[0].value[0:16], 2)/10000
b = int(poblacion[0].value[16::], 2)/10000
valores_y_individuo = []
sumatoria = 0
for i in range(len(individual.valores_x)):
    y_individuo = math.cos(
        a*individual.valores_x[i])*math.sin(b*individual.valores_x[i])
    valores_y_individuo.append(y_individuo)
    sumatoria += (abs(individual.valores_y[i]-y_individuo))
print(valores_y_individuo)
print('mejores')
print(mejores)
print('promedios')
print(promedios)
print('peores')
print(peores)

# def worst_fitness(poblacion):
#     peor = []
#     peor = sorted(poblacion, key=lambda x: x.value)
#     print(f'WORST  {poblacion}')
#     return peor



def dibujar(x, y, ya):
    plt.plot(x, color="b")
    plt.plot(y, color="red")
    plt.plot(ya, color="black")
    plt.xlabel('X')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # individual.cruza(poblacion)
    dibujar(individual.valores_x, individual.valores_y, valores_y_individuo)
