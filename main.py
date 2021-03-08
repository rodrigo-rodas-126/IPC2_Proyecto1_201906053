import xml.etree.ElementTree as ET
from xml.dom import minidom
from listacircular import ListaCiruclar
from os import system
from cola import Cola
from dato import Dato
from matriz import Matriz
from estructuras import *
import time
import os


def prettify(element, indent='  '):
    queue = [(0, element)]  # (level, element)
    while queue:
        level, element = queue.pop(0)
        children = [(level + 1, child) for child in list(element)]
        if children:
            element.text = '\n' + indent * (level+1)  # for child open
        if queue:
            element.tail = '\n' + indent * queue[0][0]  # for sibling open
        else:
            element.tail = '\n' + indent * (level-1)  # for parent close
        queue[0:0] = children  # prepend so children come before siblings


nueva_cola = Cola()
circular_binarios = ListaCiruclar()
circular_matrices = ListaCiruclar()
circular_matrices2 = ListaCiruclar()
truplas_valores = linked_list1()
nombre_archivo = ''

while True:
    time.sleep(2)
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
        circular_matrices.borra()
        ruta = input('Escribir ruta especifica: ')
        #ruta = r'C:\Users\Rodrigo\Desktop\3er año\IPC2\Laboratorio\Proyect1\Proyecto_1\entrada1.xml'
        nombre_archivo = os.path.basename(ruta)
        xml = minidom.parse(ruta)
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
            try:
                dato22 = matriz.getElementsByTagName("dato")[filas*columnas + 1]
                if (int(dato22.getAttribute('x')) > filas) or (int(dato22.getAttribute('y')) > columnas):
                    print('Error al cargar el archivo')
                    system(quit())
            except IndexError:
                pass
            for l in range(filas*columnas):
                a = True
                dato1 = matriz.getElementsByTagName("dato")[l]
                #print(valor1.getAttribute('x'))
                if (int(dato1.getAttribute('x')) > filas) or (int(dato1.getAttribute('y')) > columnas):
                    print('Error al cargar el archivo')
                    system(quit())
                else:
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
            nm_1 = Matriz(nombre, filas, columnas, prueba)
            #nm.imprimir()
            #print(nm)
            #print(prueba.string())
            #nm.imprimir()
            circular_matrices.AgregarFinal(nm)
            circular_matrices2.AgregarFinal(nm_1)
        time.sleep(2)
        if circular_matrices.size != 0:
            print('Archivo cargado con exito')
        else:
            print('Error')
        #circular_matrices.Recorrer()
        #print(circular_matrices.tamano())

    if comando == '2':
        conta_ma = 0
        truplas_valores.borrar()
        nombres_lista = circular_matrices.Recorrer_String()
        time.sleep(2)
        print('Accediendo a matrizes')
        time.sleep(1)
        print('', end='.')
        time.sleep(1)
        print('', end='.')
        time.sleep(1)
        print('', end='.')
        print('\n')
        for numas in range(nombres_lista.devolver_tamano2()):
            #respuestas_reducidas = []
            nom_buscar = nombres_lista.buscar_indice(numas)
            matri_auxiliar = circular_matrices.Listar(nom_buscar)
            new_n = matri_auxiliar.n
            new_m = matri_auxiliar.m
            #matri_auxiliar.binario()
            respuestas_reducidas = (matri_auxiliar.binario())
            #print(respuestas_reducidas[0])
            #print(respuestas_reducidas[1])
            circular_binarios.AgregarFinal(respuestas_reducidas[0])
            truplas_valores.insertar(respuestas_reducidas[1])
            #print(truplas_valores.string())
            #print(circular_binarios.)

    if comando == '3':
        ruta_salida = input('Direccion: ')
        time.sleep(2)
        print('Generando archivo de salida')
        root_1 = ET.Element("matrices")
        contador_frec = -1
        nombres_lista_1 = circular_binarios.Recorrer_String()
        contador_new = -1
        for numasa in range(nombres_lista_1.devolver_tamano2()):
            contador_new += 1
            contador_frec += 1
            cord_x = 0
            cord_y = 0
            nom_buscar_1 = nombres_lista_1.buscar_indice(numasa)
            matri_auxiliar_1 = circular_binarios.Listar(nom_buscar_1)
            matrt = ET.SubElement(root_1, "matriz", nombre=str(matri_auxiliar_1.nombre),
                                  n=str(matri_auxiliar_1.n),
                                  m=str(matri_auxiliar_1.m),
                                  g=str(truplas_valores.buscar_indice(contador_new).devolver_tamano() + 1))
            for amin in range(matri_auxiliar_1.n):
                cord_x += 1
                cord_y = 0
                datos_aux_1 = matri_auxiliar_1.linked_list1.buscar_indice(amin)
                for snom in range(matri_auxiliar_1.m):
                    cord_y += 1
                    dato_aux = datos_aux_1.buscar_indice(snom)
                    dato_1 = ET.SubElement(matrt, "dato", x=str(cord_x), y=str(cord_y))
                    dato_1.text = str(dato_aux)
            #for ago in range(truplas_valores.devolver_tamano()):
            tup_aux = truplas_valores.buscar_indice(contador_frec)
            for agoi in range(tup_aux.devolver_tamano1()):
                tupit = tup_aux.buscar_indice(agoi)
                if tupit != 0:
                    frecu = ET.SubElement(matrt, "frecuencia", g=str(agoi+1))
                    frecu.text = str(tupit-1)
                else:
                    continue
        prettify(root_1)
        arbolito = ET.ElementTree(root_1)
        #arbolito.write(ruta_salida+'\salida_reporte.xml')
        arbolito.write(str(ruta_salida)+str(nombre_archivo)+'_reporte.xml')
        time.sleep(4)
        print('Archivo de salida generado')
        time.sleep(2)

    if comando == '4':
        print('>>Jose Rodrigo Rodas Palencia')
        print('>>201906053')
        print('>>Introduccion a la programación y computación 2, sección "E"')
        print('>>Ingenieria en Ciencias y Sistemas')
        print('>>4to Semetre')

    if comando == '5':
        """
        if opcion1 == 'S':
            conta_ma2 = 0
            with open('grafos/grafo_'+nombre_archivo+'.dot', 'w') as re:
                re.write('digraph G {' + '\n')
                re.write('splines="False";' + '\n')
                re.write('/* Entidades */' + '\n')
                re.write('Matrizes [label="matrices", shape="oval"]' + '\n')

                nombres_lista2 = circular_matrices2.Recorrer_String()
                for numas in range(nombres_lista2.devolver_tamano2()):
                    conta_ma2 += 1
                    nom_buscar2 = nombres_lista2.buscar_indice(numas)
                    mat = circular_matrices2.Listar(nom_buscar2)

                    re.write(str(mat.nombre)+'[label="' + str(mat.nombre) + '", shape="oval"]' + '\n')
                    re.write('N_'+str(mat.nombre)+'[label="n=' + str(mat.n) + '", shape="doublecircle", color="blue"]' + '\n')
                    re.write('M_'+str(mat.nombre)+'[label="m=' + str(mat.m) + '", shape="doublecircle", color="blue"]' + '\n')

                    re.write('/* Relaciones */' + '\n')
                    re.write('Matrizes -> '+str(mat.nombre)+'\n')
                    re.write(str(mat.nombre)+' -> N_'+str(mat.nombre)+'\n')
                    re.write(str(mat.nombre)+' -> M_'+str(mat.nombre)+'\n')

                    conta_ma1 = -1
                    cont_1 = -1
                    for sa in range(mat.n):
                        conta_ma1 += 1
                        aux = mat.linked_list1.buscar_indice(sa)
                        for se in range(mat.m):
                            cont_1 += 1
                            if conta_ma1 == 0:
                                re.write(
                                    'AUX_'+str(mat.nombre)+'_'+str(cont_1)+' [label="' + str(
                                        aux.buscar_indice(se)) + '", shape="circle"]' + '\n')
                                re.write(str(mat.nombre)+' -> ' + 'AUX_'+str(mat.nombre)+'_'+str(cont_1) + '\n')
                            elif conta_ma1 <= mat.n:
                                anterior = aux.buscar_indice(conta_ma1 - 1)
                                re.write(
                                    'AUX_'+str(mat.nombre)+'_'+ str(cont_1) + ' [label="' + str(
                                        aux.buscar_indice(se)) + '", shape="circle"]' + '\n')
                                re.write('AUX_'+str(mat.nombre)+'_'+str(cont_1 - mat.m) + ' -> ' + 'AUX_'+str(mat.nombre)+'_'+str(cont_1) + '\n')
                re.write('}')
            re.close()
            os.system('dot -Tpng ' + 'grafos/grafo_'+nombre_archivo+'.dot' + ' -o grafos/imagen_'+nombre_archivo+'.png')
        elif opcion1 == 'N':
        """
        graf = input('Nombre de la matriz: ')
        try:
            ma_graf = circular_matrices2.Listar(graf)
            time.sleep(2)
            print('Generando Grafo')
            ma_graf.grafico()
            time.sleep(2)
            print('Grafo Generando ')
        #print(ma_graf.nombre)
        except:
            print('Error! Matriz inexistenete')

    if comando == '6':
        system(quit())
