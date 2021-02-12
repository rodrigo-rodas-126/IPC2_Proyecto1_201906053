import xml.etree.ElementTree as ET
from xml.dom import minidom
from listacircular import ListaCiruclar
from os import system

"""
lista = ListaCiruclar()
lista.AgregarFinal(10)
lista.AgregarFinal(110)
lista.AgregarFinal(130)
lista.AgregarFinal(20)
lista.AgregarInicio(12)
lista.Recorrer()
"""

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
        #ruta = input('Escribir ruta especifica: ')
        xml = minidom.parse('entrada.xml')
        matrices = xml.getElementsByTagName("matriz")
        for matriz in matrices:
            if matriz.hasAttribute("name"):
                nombre = matriz.getAttribute('name')
                if matriz.hasAttribute("n"):
                    fil = matriz.getAttribute('n')
                    if matriz.hasAttribute("m"):
                        col = matriz.getAttribute('m')
                        print('Matriz: ' + nombre +' n:' +fil+' m:'+col)
                        for i in range(int(fil)*int(col)):
                            valor1 = matriz.getElementsByTagName("dato")[i]
                            print(valor1.firstChild.data)

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
        pass

    if comando == '6':
        system(quit())