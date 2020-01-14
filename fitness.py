import math
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

def fitness(a,b):
    valores_y_individuo=[]
    sumatoria=0
    for i in range(len(valores_x)):
        y_individuo=math.cos(a*valores_x[i])*math.sin(b*valores_x[i])
        valores_y_individuo.append(y_individuo)
        sumatoria+=(abs(valores_y[i]-y_individuo))
    return sumatoria
fitness(2.1,3.1)
