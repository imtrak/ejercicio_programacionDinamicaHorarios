import numpy as np
from numpy.core.multiarray import empty_like
from numpy.core.numeric import True_, indices

def funcionOptimizacion (num_act, horarios):
    dia = 24
    vectorB = []

    solucion = subConjuntos(horarios)
    solucionAux = []
    for x in solucion:
        solucionAux.append(conjuntoSinInterseccion(x))
    
    for x in solucionAux:
        vectorB.append(calculoBeneficio(x))
            
    indiceMayor = encontrarIndiceMayor(vectorB)


    listActs = encontrarActividad(horarios,solucionAux[indiceMayor])

    print(listActs)
    print(vectorB[indiceMayor])
def encontrarActividad(horario1, horario2):
    listaActs = []

    for x in range(len(horario2)):
        for y in range(len(horario1)):
            if horario2[x] == horario1[y]:
                listaActs.append(y+1)
    return listaActs        
    
def encontrarIndiceMayor(vectorB):
    mayor = 0
    indice = 0
    for x in range(len(vectorB)):
        if vectorB[x] > mayor:
            mayor = vectorB[x]
            indice = x

            
    return indice




def calculoBeneficio(horarios):
    suma = 0
    vectorB = []
    if horarios:
        for x in horarios:
            vectorB.append(abs(x[0]-x[1]))

        for y in vectorB:
            suma = suma+y
    
    return suma

def conjuntoSinInterseccion(conjunto):

    if len(conjunto) >= 2:
        for x in range(len(conjunto)):
            for y in range(x + 1,len(conjunto)):
                if interseccion(conjunto[x],conjunto[y]):
                    return []
        return conjunto            
    else:
        if conjunto:
            return conjunto
    

def interseccion(hora1,hora2):
    if hora1[0] > hora2[0] and hora1[0] < hora2[1]:
        return True
    if hora2[0] > hora1[0] and hora2[0] < hora1[1]:
        return True
    if hora1[0] == hora2[0] and hora1[1] == hora2[1]:
        return True
    if hora1[0] == hora2[0]:
        return True
    else:
        return False



def solucionar(beneficio, horarios):
    for e in sorted(horarios, key=lambda s: (len(s), s)):
        print(e)

def subConjuntos(conjunto):
    return subconjunto_recursivo([], conjunto)

def subconjunto_recursivo(actual,conjunto):
    if conjunto:
        return subconjunto_recursivo(actual,conjunto[1:])+ subconjunto_recursivo(actual+[conjunto[0]],conjunto[1:])
    return [actual]



funcionOptimizacion(5, [[2,5],[7,22],[22,24],[22,23],[23,24]]) #esperado 1 2 4 5

funcionOptimizacion(5, [[1,10],[7,9],[9,14],[10,20],[20,24]]) #esperado 1 4 5

funcionOptimizacion(4, [[1,6], [6,24], [20,22], [22,23]]) # Esperado 1, 2

funcionOptimizacion(10, [[1,3], [3,6], [4,10], [9,12], [10,13], [10,20], [14,18], [18,22], [20,24], [22,24]])# Esperado 1 3 6 9

funcionOptimizacion(8, [[1,3], [3,7], [8,13], [13,15], [16,18], [18,21], [21,22], [22,24]])# Esperado 1 2 3 4 5 6 7 8

funcionOptimizacion(7, [[2,5], [4,7], [7,13], [12,15], [16,19], [18,21], [21,23]]) # 2 3 6 7