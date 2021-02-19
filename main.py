import xml.etree.ElementTree as ET
from xml.dom import minidom
from listacircular import ListaCiruclar
from os import system
from cola import Cola
from dato import Dato
from matriz import Matriz
from estructuras import *

datos = []
nueva_cola = Cola()

while True:
    print('\n')
    print('======Menu======')
    print('1.Cargar Archivo')
    print('2.Procesar Archivo')
    print('3.Escribir Archivo de Salida')
    print('4.Mostrar datos del estudiante')
    print('5.Generar gràfica')
    print('6.Salir')
    print('===============')
    comando = input('Ingrese opcion: ')
    print('\n')

    if comando == '1':
        contador = 0
        circular_matrices = ListaCiruclar()
        #ruta = input('Escribir ruta especifica: ')
        xml = minidom.parse('entrada2.xml')
        matrices = xml.getElementsByTagName("matriz")
        for matriz in matrices:
            contador += 1
            #print(contador)
            prueba = linked_list1()
            #if matriz.hasAttribute("name"):
            nombre = matriz.getAttribute('nombre')
            #print(nombre)
                #if matriz.hasAttribute("n"):
            filas = int(matriz.getAttribute('n'))
                    #if matriz.hasAttribute("m"):
            columnas = int(matriz.getAttribute('m'))
                        #print('Matriz: ' + nombre+' n:'+str(filas)+' m:'+str(columnas))
            for l in range(filas*columnas):
                dato1 = matriz.getElementsByTagName("dato")[l]
                #print(valor1.getAttribute('x'))
                aw = Dato(dato1.getAttribute('x'), dato1.getAttribute('y'), dato1.firstChild.data)
                nueva_cola.encolar(aw)
            #nueva_cola.imprimir()
            for i in range(1, filas+1):
                a = linked_list()
                for j in range(1, columnas+1):
                    valor1 = nueva_cola.desencolar()
                    #print('\n')
                    #nueva_cola.imprimir()
                    a.insertar(valor1.valor)
                prueba.insertar(a)
            nm = Matriz(nombre, filas, columnas, prueba)
            #nm.imprimir()
            #print(nm)
            #print(prueba.string())
            circular_matrices.AgregarFinal(nm)
        #circular_matrices.Recorrer()

    if comando == '2':
        pass

    if comando == '3':
        pass

    if comando == '4':
        print('>>Jose Rodrigo Rodas Palencia')
        print('>>201906053')
        print('>>Introduccion a la programación y computación 2, sección "E"')
        print('>>Ingenieria en Ciencias y Sistemas')
        print('>>4to Semetre')

    if comando == '5':
        graf = input('Nombre de la matriz: ')
        ma_graf = circular_matrices.Listar(graf)
        ma_graf.grafico()

    if comando == '6':
        system(quit())
