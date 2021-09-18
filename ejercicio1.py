import numpy as np
from numpy.core.multiarray import empty_like
from numpy.core.numeric import True_

def funcionOptimizacion (num_act, horarios):
    dia = 24
    vectorB = calculoBeneficio(horarios)

    solucion = solve_knapsack(vectorB,vectorB,horarios,dia)
    print(solucion)
    aux = ""
    for i in range(np.size(solucion[1])):
        x=solucion[1][i]
        if x != x + 1:
            if x != 0:
                aux= aux+str(i+1)+" " 
    print(aux)

def calculoBeneficio(horarios):
    vectorB = []

    for x in horarios:
        vectorB.append(abs(x[0]-x[1]))
    
    return vectorB

def interseccion(hora1,hora2):
    if hora1[0] >= hora2[0] and hora1[0] < hora2[1]:
        return True
    if hora2[0] >= hora1[0] and hora2[0] < hora1[1]:
        return True
    else:
        return False

def solve_knapsack(profits, weights, horarios ,capacity):
  dp = np.zeros((capacity + 1,len(profits)))
  return knapsack_recursive(dp, profits, weights, horarios, -1 ,capacity, 0)



def knapsack_recursive(dp, profits, weights, horarios, horarioIndex,capacity, currentIndex):
    
  # base checks
  if capacity <= 0 or currentIndex >= len(profits):
    return [0,dp[capacity]]

  if horarioIndex > -1:
    if interseccion(horarios[horarioIndex], horarios[currentIndex]):
        return knapsack_recursive(dp, profits, weights, horarios,horarioIndex,capacity, currentIndex + 1)


  # if we have already solved a similar problem, return the result from memory
  if dp[capacity][currentIndex] != 0:
    return [dp[capacity][currentIndex],dp[capacity]]

  # recursive call after choosing the element at the currentIndex
  # if the weight of the element at currentIndex exceeds the capacity, we
  # shouldn't process this
  profit1 = 0
  if weights[currentIndex] <= capacity:
    aux =  knapsack_recursive(dp, profits, weights, horarios, horarioIndex + 1,capacity - weights[currentIndex], currentIndex + 1)
    profit1 = profits[currentIndex] + aux[0]

  # recursive call after excluding the element at the currentIndex
  profit2 = knapsack_recursive(
    dp, profits, weights, horarios, horarioIndex + 1,capacity, currentIndex + 1)
  
  dp[capacity][currentIndex] = max(profit1, profit2[0])

  return [dp[capacity][currentIndex],dp[capacity]]


funcionOptimizacion(5, [[2,5],[7,22],[22,24],[22,23],[23,24]]) #esperado 1 2 3

funcionOptimizacion(5, [[1,10],[7,9],[9,14],[10,20],[20,24]]) #esperado 1 4 5

funcionOptimizacion(4, [[1,6], [6,24], [20,22], [22,23]]) # Esperado 1, 2

funcionOptimizacion(10, [[1,3], [3,6], [4,10], [9,12], [10,13], [10,20], [14,18], [18,22], [20,24], [22,24]])# 23

funcionOptimizacion(8, [[1,3], [3,7], [8,13], [13,15], [16,18], [18,21], [21,22], [22,24]])# 21

