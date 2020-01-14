import random
import math

class Individuo:
    def __init__(self,value,fitness,probability):
        self.value=value
        self.fitness=fitness
        self.probability=probability
    def __repr__(self):
        return '{'+str(self.value)+','+str(self.fitness)+','+str(self.probability)+'}'

valores_x=[
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
valores_y=[
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
def fitness(value):
    a = int(value[0:13],2)/1000
    b = int(value[13::],2)/1000
    valores_y_individuo=[]
    sumatoria=0
    for i in range(len(valores_x)):
        y_individuo=math.cos(a*valores_x[i])*math.sin(b*valores_x[i])
        valores_y_individuo.append(y_individuo)
        sumatoria+=(abs(valores_y[i]-y_individuo))
    return sumatoria

def mutar(individuo):
    probabilidad_mutar=1/2
    array_individuo=list(individuo)
    index=0
    for bit in array_individuo:
        azar_mutar=random.random()
        if azar_mutar<=probabilidad_mutar:
            if bit == '1':
                array_individuo[index]='0'
            else:
                array_individuo[index]='1'
        index+=1
    
    return ''.join(array_individuo)

def conv_binario(dec):
    decode=[]
    final=''
    if dec==0:
        decode.insert(0,'0')
    else:
        while dec!=0:
            if int(dec) % 2 !=0:
                decode.insert(0,'1')
            else:
                decode.insert(0,'0')
            dec=int(dec/2)
    while len(decode) !=13:
        decode.insert(0,'0')
    for n in decode:
        final+=n
    return final
poblacion=[]
for _ in range(16):
    value=conv_binario(random.randint(1,5999))+conv_binario(random.randint(1,5999))
    poblacion.append(Individuo(value,fitness(value),0))

poblacion = sorted(poblacion, key=lambda x: x.fitness)




for _ in range(2000):
    fitness_sum = sum([ind.fitness for ind in poblacion])
    probability_offset = 0

    for ind in poblacion:
        ind.probability = probability_offset + (ind.fitness / fitness_sum)
        probability_offset += ind.probability
   

    children=[]
    for padre in poblacion:
        parent_1=poblacion[0]
        parent_2=poblacion[0]
        rand = random.random()
        for ind in poblacion:
            if ind.probability > rand and ind.probability<1:
                parent_1=ind
                break
        rand = random.random()
        for ind in poblacion:
            if ind.probability > rand and ind.probability<1:
                parent_2=ind
                break
        indice_cruza=random.randint(1,24)
        value1=parent_1.value[0:indice_cruza]+parent_2.value[indice_cruza:26]
        value2=parent_2.value[0:indice_cruza]+parent_1.value[indice_cruza:26]
        children.append(Individuo(value1,0,0))
        children.append(Individuo(value2,0,0))
        
    poblacion+=children
    mejor_poblacion=[]
    for individuo in poblacion:
        prob_mutar=1/2
        azar=random.random()
        if azar<=prob_mutar:
            individuo.value=mutar(individuo.value)
        a = int(individuo.value[0:13],2)/1000
        b = int(individuo.value[13::],2)/1000
      
        if a<6 and b<6:
            individuo.fitness=fitness(individuo.value)
            mejor_poblacion.append(individuo)  
    sorted_ind = sorted(mejor_poblacion, key=lambda x: x.fitness)
    poblacion=sorted_ind[0:16]
    print(poblacion[0])
    print(int(individuo.value[0:13],2)/1000)
    print(int(individuo.value[13::],2)/1000)

print(poblacion[0])
print(int(individuo.value[0:13],2)/1000)
print(int(individuo.value[13::],2)/1000)

