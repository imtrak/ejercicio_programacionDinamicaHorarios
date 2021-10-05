file=open("prueba.txt","r")
string1 = file.read()
lineas = string1.split('\n')
num_actividades=int(lineas[0])


horarios=[[0]*3]*num_actividades

for i in range(num_actividades):
  aux=lineas[i+1]
  horarios[i]=aux.split(' ')
file.close()

sl=[horarios[i][1:3] for i in range(num_actividades)]

for x in range(num_actividades):
  for y in range(2):
    sl[x][y]=int( sl[x][y])


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

funcionOptimizacion(num_actividades,sl)
