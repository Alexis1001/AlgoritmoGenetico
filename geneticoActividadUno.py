import random
from random import randint
import math
import numpy as np


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
    print("los indivudos son fitness XXX ",individuos)
    xi=[]
    yi=[]
    tamanio=len(individuos[0])
    puntomedio=int(tamanio/2)
    archivoDeLasX=open("x.txt", "r")
    xi=archivoDeLasX.readlines()
    archivoDeLasX.close()
    archivoDeLasY=open("y.txt","r")
    yi=archivoDeLasY.readlines()
    archivoDeLasX.close()
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
        print("numeroA ",numeroA)
        print("numeroB ",numeroB)
        for k in range(len(xi)):
            x=float(xi[k])
            y=float(yi[k])
            print(" x = ",x," y = ",y,end='\n')
            fit_ness=abs(y-(math.cos(math.radians(numeroA*x)))*(math.sin(math.radians(numeroB*x))))
            resultado=round(fit_ness,3)
            print(resultado)          
            sumatoriaFintness=sumatoriaFintness+resultado
        listaFitness.append(round(sumatoriaFintness,3)) #aqui guardo la sumatoria del fitnes de cada individuo 
        sumatoriaFintness=0 
    print(listaFitness)
    tamanioInicialPoblacion=len(individuos) 
    ruleta(individuos,listaFitness,tamanioInicialPoblacion)          

def ruleta(individuos,listaFitness,tamanioInicialPoblacion):
    #print("el fitnees de los individuos es ",end='\n')
    #print(listaFitness)
    arregloFitness=np.array(listaFitness)
    sumaTotalFitness=np.sum(arregloFitness)
    fitnessTotal=round(sumaTotalFitness,3)
    intervalos=[]
    sumaIntervalos=0
    print("Total finnes ",fitnessTotal)
    for i in range(len(listaFitness)):
        divicionFitness=round(arregloFitness[i]/fitnessTotal,3)
        sumaIntervalos=round(sumaIntervalos+divicionFitness,3)
        print("fitness ",i," numero ",arregloFitness[i],"/",fitnessTotal," = ",divicionFitness,"intervalos ",sumaIntervalos)
        intervalos.append(sumaIntervalos)
    print(intervalos)
    nuevaGeneracion=0
    encontrado_aleatorio_1=False
    encontrado_aleatorio_2=False
    individuo1Acruzar=0
    individuo2Acruzar=0
    ListaNuevosPadres=[]
    while nuevaGeneracion<tamanioInicialPoblacion :
        aleatorio_1=round(random.random(),3)
        aleatorio_2=round(random.random(),3)

        for k in range(len(intervalos)) :
            if k==0 and aleatorio_1<=intervalos[k] :
                individuo1Acruzar=k
                encontrado_aleatorio_1=True
            
            if aleatorio_1<=intervalos[k] and aleatorio_1>=intervalos[k-1]:
                individuo1Acruzar=k
                encontrado_aleatorio_1=True
            
            if k==0 and aleatorio_2<=intervalos[k] :
                individuo2Acruzar=k
                encontrado_aleatorio_2=True
            
            if aleatorio_2<=intervalos[k] and aleatorio_2>=intervalos[k-1]:   
                individuo2Acruzar=k
                encontrado_aleatorio_2=True
            
            if(encontrado_aleatorio_1==True and encontrado_aleatorio_2==True):
                print("cruzamiento individuo [1] ",individuo1Acruzar," con "," individuo [2] ",individuo2Acruzar)
                break    
        encontrado_aleatorio_1=False
        encontrado_aleatorio_2=False
        print("individuo ",individuos[individuo1Acruzar]," cruza con individuo ",individuos[individuo2Acruzar]) 
        #aqui mando los individuos que voy a cruzar
        nuevosPadres=cruza_mutacion(individuos[individuo1Acruzar],individuos[individuo2Acruzar])    
        if len(nuevosPadres)==1 :
            padre1=nuevosPadres[0]
            ListaNuevosPadres.append(padre1)
        if len(nuevosPadres)==2: #aqui debe de ir la condicion perro de cuando tengo 9 y salgan 2
            if len(ListaNuevosPadres)==tamanioInicialPoblacion-1:
                padre2=nuevosPadres[0]
                ListaNuevosPadres.append(padre2)
            else:
                padre2=nuevosPadres[0]
                ListaNuevosPadres.append(padre2)
                padre3=nuevosPadres[1]
                ListaNuevosPadres.append(padre3)     
        nuevaGeneracion=nuevaGeneracion+len(nuevosPadres)

    print("tamanio de nuevos padres en la ruleta ",len(ListaNuevosPadres))
    print(ListaNuevosPadres)
    Iteraciones(ListaNuevosPadres)

       
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

def Iteraciones(ListaNuevosPadres):

    print("iteracion en el metodo iteraciones ",iterar)
    iterar.append("1")
    print("lista de los padre en el metodo iteraciones ")
    print(ListaNuevosPadres)
    print("el tamanio de la poblacion es en el metodo iteraciones ",len(ListaNuevosPadres))
    print("total de generacion ",TotalDegeneraciones)
    if len(iterar)<=TotalDegeneraciones:
        print("seguir iterando ")
        fitness(ListaNuevosPadres)
    else:
        print("interrumpido perrro")
        


def main ():
    individuos=generandoPoblacion(10,12)
    fitness(individuos)
    

ProbabilidadMutacion=30
minimos=[]
maximos=[]
promedios=[]
iterar=[]
TotalDegeneraciones=2
IteracionPorGeneracion=1
main()

