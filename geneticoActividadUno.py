import random
from random import randint
import math
import numpy as np
import scipy as sp
import matplotlib.pylab as plt


def generandoPoblacion(poblacionInicial,tamanioGenotipo):
    poblacionInicial=poblacionInicial
    tamanioGenotipo=tamanioGenotipo
    Padres=0
    individuos=[]
    individuo=[]
    while Padres<poblacionInicial :
        for i in range(tamanioGenotipo) :
            gen=randint(0,1)
            individuo.append(gen)
        parteA=individuo[0:6]
        parteB=individuo[6:12]
        BinarioA=''.join(map(str,parteA))
        BinarioB=''.join(map(str,parteB))
        decimalA=int(BinarioA,2)
        decimalB=int(BinarioB,2)
        if(decimalA>0 and decimalA<60 and decimalB>0 and decimalB<60):
            copia=individuo[:]
            individuos.append(copia)
            Padres=Padres+1 
        else :
            print(" ") 
        individuo.clear()  
    return individuos

def  fitness(individuos):
    iterar.append("1")
    if len(iterar)==TotalDegeneraciones+1:
        print("total de generaciones es ",len(iterar))
        graficarMejoresPeoresPromedios(maximos,minimos,promedios)        
    else:
        tamanio=len(individuos[0])
        puntomedio=int(tamanio/2)
        xi=VALORES_X
        yi=VALORES_Y
        sumatoriaFintness=0
        listaFitness=[]
        for j in range(len(individuos)):
            print("pocicion de j ",j)
            individuo=individuos[j]
            parteA=individuo[0:puntomedio]
            parteB=individuo[puntomedio:tamanio]
            BinarioA=''.join(map(str,parteA))
            BinarioB=''.join(map(str,parteB))
            decimalA=int(BinarioA,2)
            decimalB=int(BinarioB,2)
            print("parte   A ",BinarioA," parte   B ",BinarioB,end='\n')
            print("decimal A ",decimalA," decimal B ",decimalB,end='\n')
            numeroA=decimalA*0.1
            numeroB=decimalB*0.1
            cordenadasY=[]
            for k in range(len(xi)):
                x=float(xi[k])
                y=float(yi[k])
                print(" x = ",x," y = ",y,end='\n')
                fit_ness=abs(y-(math.cos(math.radians(numeroA*x)))*(math.sin(math.radians(numeroB*x))))
                resultado=round(fit_ness,3)
                print(resultado)     
                sumatoriaFintness=sumatoriaFintness+resultado
                if len(iterar)==TotalDegeneraciones:#nuevo
                    y_prima=(y-(math.cos(math.radians(numeroA*x)))*(math.sin(math.radians(numeroB*x))))
                    #y_prima=(math.cos(math.radians(numeroA*x)))*(math.sin(math.radians(numeroB*x)))
                    cordenada_y=round(y_prima,4)
                    cordenadasY.append(cordenada_y)
            listaFitness.append(round(sumatoriaFintness,3)) #aqui guardo la sumatoria del fitnes de cada individuo 
            sumatoriaFintness=0
            if len(iterar)==TotalDegeneraciones: #nuevo
                Mejores_Y.append(cordenadasY) 
        tamanioInicialPoblacion=len(individuos) 
        maximo_valor=max(listaFitness)
        maximos.append(maximo_valor)
        minimo_valor=min(listaFitness)
        minimos.append(minimo_valor)
        sumatoria =sum(listaFitness)
        longitud =float(len(listaFitness))
        promedio = sumatoria / longitud
        promedios.append(promedio)
        ruleta(individuos,tamanioInicialPoblacion,listaFitness)

def ruleta(lista_individuos,tamanioInicialPoblacion,listaFitness):    
    lista_Normal=np.array(listaFitness) 
    lista_mayor_a_menor=listaFitness  
    lista_mayor_a_menor.sort(reverse=True) 
    suma_por_fitnnes=0
    lista_suma_fitnnes=[]
    for i in range(len(lista_mayor_a_menor)):
        suma_por_fitnnes=suma_por_fitnnes+lista_mayor_a_menor[i]
        lista_suma_fitnnes.append(suma_por_fitnnes)
        
    suman_total_lista=sum(lista_suma_fitnnes)
    lista_porcentajes=[]
    for k in range(len(lista_suma_fitnnes)):
        porcentaje=int(lista_suma_fitnnes[k]/suman_total_lista*100)
        lista_porcentajes.append(porcentaje)

    array_porcentajes=np.array(lista_porcentajes)
    lista_mayor_a_menor_porcentaje=lista_porcentajes  
    lista_mayor_a_menor_porcentaje.sort(reverse=True)       

    intervalos=[]
    suma_intervalos=0
    for x in range(len(lista_mayor_a_menor_porcentaje)):
        suma_intervalos=suma_intervalos+lista_mayor_a_menor_porcentaje[x]
        intervalos.append(suma_intervalos)    
    suma_total_porcentajes=np.sum(array_porcentajes)
    
    encontrado_aleatorio_1=False
    encontrado_aleatorio_2=False
    aleatorio_1=0
    aleatorio_2=0
    individuo1Acruzar=0
    individuo2Acruzar=0
    individuos=0
    individuo_cruzar1=0
    individuo_cruzar2=0
    ListaNuevosPadres=[]
    while individuos<tamanioInicialPoblacion:
        
        aleatorio_1=random.randint(0,suma_total_porcentajes)
        aleatorio_2=random.randint(0,suma_total_porcentajes)
        for k in range(len(intervalos)) :
            if k==0 and aleatorio_1<=intervalos[k] :
                individuo1Acruzar=k
                encontrado_aleatorio_1=True
            
            if aleatorio_1<=intervalos[k] and aleatorio_1>intervalos[k-1]:
                individuo1Acruzar=k
                encontrado_aleatorio_1=True
            
            if k==0 and aleatorio_2<=intervalos[k] :
                individuo2Acruzar=k
                encontrado_aleatorio_2=True

            if aleatorio_2<=intervalos[k] and aleatorio_2>intervalos[k-1]:   
                individuo2Acruzar=k
                encontrado_aleatorio_2=True
            
            if(encontrado_aleatorio_1==True and encontrado_aleatorio_2==True):
                
                individuo1=lista_mayor_a_menor_porcentaje[individuo1Acruzar]
                individuo2=lista_mayor_a_menor_porcentaje[individuo2Acruzar]
                 
                for  k in range(len(array_porcentajes)):
                    if array_porcentajes[k]==individuo1 :
                        break
                for m in range(len(array_porcentajes)):
                    if  array_porcentajes[m]==individuo2 :        
                        break 
                pocion_del_individuo1=lista_Normal[k]
                pocion_del_individuo2=lista_Normal[m]
                for n in range(len(lista_Normal)):
                    if lista_Normal[n]==pocion_del_individuo1:
                        individuo_cruzar1=n
                        break
                for m in range(len(lista_Normal)):
                    if lista_Normal[m]==pocion_del_individuo2:
                        individuo_cruzar2=m
                        break
                break  
        encontrado_aleatorio_1=False
        encontrado_aleatorio_2=False
        nuevosPadres=cruza_mutacion(lista_individuos[individuo_cruzar1],lista_individuos[individuo_cruzar2])    
        if len(nuevosPadres)==1 :
            padre1=nuevosPadres[0]
            ListaNuevosPadres.append(padre1)
        if len(nuevosPadres)==2: #aqui debe de ir la condicion de cuando tengo 9 y salgan 2 y mi poblacion es de 10
            if len(ListaNuevosPadres)==tamanioInicialPoblacion-1:
                padre2=nuevosPadres[0]
                ListaNuevosPadres.append(padre2)
            else:
                padre2=nuevosPadres[0]
                ListaNuevosPadres.append(padre2)
                padre3=nuevosPadres[1]
                ListaNuevosPadres.append(padre3)     
        individuos=individuos+len(nuevosPadres)
    fitness(ListaNuevosPadres)
   
def cruza_mutacion(padre,madre):
    nuevosPadres=[]
    tamanio=len(padre)
    puntomedio=int(tamanio/2)
    aleatorioCruza=random.randint(puntomedio-2,puntomedio+2)
    parteA1=padre[0:aleatorioCruza]
    parteA2=padre[aleatorioCruza:]
    parteB1=madre[0:aleatorioCruza]
    parteB2=madre[aleatorioCruza:]
    hijo1=parteA1+parteB2
    hijo2=parteB1+parteA2

    for i in range(len(hijo1)):
        numero=random.randint(0,100)
        if(numero<=ProbabilidadMutacion):
            if(hijo1[i]==0):
                hijo1[i]=1
            else:
                hijo1[i]=0   

    for i in range(len(hijo2)):
        numero=random.randint(0,100)
        if(numero<=ProbabilidadMutacion):
            if(hijo2[i]==0):
                hijo2[i]=1
            else:
                hijo2[i]=0                       

    hijo1A=hijo1[0:puntomedio]
    hijo1B=hijo1[puntomedio:tamanio]
    hijo2A=hijo2[0:puntomedio]
    hijo2B=hijo2[puntomedio:tamanio]
    decimalHijo1A=int(''.join(map(str,hijo1A)),2)
    decimalHijo1B=int(''.join(map(str,hijo1B)),2)
    decimalHijo2A=int(''.join(map(str,hijo2A)),2)
    decimalHijo2B=int(''.join(map(str,hijo2B)),2)

    if((decimalHijo1A>0 and decimalHijo1A<60)and(decimalHijo1B>0 and decimalHijo1B<60)):
        nuevosPadres.append(hijo1)

    if((decimalHijo2A>0 and decimalHijo2A<60) and (decimalHijo2B>0 and decimalHijo2B<60)):
        nuevosPadres.append(hijo2)   

    return nuevosPadres  
      
def graficarMejoresPeoresPromedios(maximos,minimos,promedios):
    
    sumaFitnnesIndividuo=[]
    mejor=0
    for a in range(len(Mejores_Y)):
        suma=sum(Mejores_Y[a])
        sumaFitnnesIndividuo.append(round(suma,4))
    mejor=min(sumaFitnnesIndividuo)
    posicion=sumaFitnnesIndividuo.index(mejor)
    Cordenadas_Y=Mejores_Y[posicion]

    print("Y del profe ")
    print(VALORES_Y)
    print("Y del algoritmo ")
    print(Cordenadas_Y)
    """Cordenadas_Y.pop(0)
    Cordenadas_Y.insert(0,0.0)""" 
    plt.subplot(221)
    plt.title("fitnnes")
    plt.plot(maximos, linestyle='-', label = "peores")
    plt.plot(promedios,linestyle='-', label = "promedios")
    plt.plot(minimos,linestyle='-', label = "mejores")
    plt.xlabel("generacion")  
    plt.ylabel("cordenada") 
    plt.legend()
   
    plt.subplot(222)
    plt.title("valores reales y generados")
    plt.plot( VALORES_X,VALORES_Y,linestyle='-', label = "original")
    plt.plot(VALORES_X,Cordenadas_Y,linestyle='-', label = "generados")
    plt.xlabel("abscisa")  
    plt.ylabel("cordenada") 
    plt.legend()
    plt.show()

def main ():
    individuos=generandoPoblacion(10,12)
    fitness(individuos)
    

ProbabilidadMutacion=30
minimos=[]
maximos=[]
promedios=[]
VALORES_X=[0, .25, .5, .75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.25, 4.5, 4.75, 5]
VALORES_Y=[0.0718, 0.8103, 0.5631, 0.0818, 0.3868, 0.8400, 0.3484, -0.5434, -0.5749, -0.0151, -0.0825, -0.6369, -0.4434, 0.4821, 0.8186, 0.2972, 0.1137, 0.6506, 0.7561, -0.0776, -0.6942]
iterar=[]
fitnessTotalPorIndividuo=[]
TotalDegeneraciones=50
Mejores_Y=[]
main()

#alone heart
#scorpion