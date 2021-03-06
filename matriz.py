from estructuras import *
import os
import time


class Matriz():

    def __init__(self, nombre, n, m, linked_list1):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.linked_list1 = linked_list1

    def imprimir(self):
        print('Nombre: '+str(self.nombre)+' '+', n: '+str(self.n)+' '+', m: '+str(self.m))
        self.linked_list1.imprimir()

    def tuplas(self):
        pass

    def binario(self):
        frecuencias = linked_list()
        contador_a = -1
        bina = linked_list1()
        tuplada = linked_list1()
        coordenadas = linked_list()
        bina.borrar()
        tuplada.borrar()
        cont_b = -1

        time.sleep(2)
        print('Procesando Matriz')
        for sa in range(self.linked_list1.devolver_tamano()):
            bina_aux = linked_list()
            cont_b += 1
            aux = self.linked_list1.buscar_indice(sa)
            time.sleep(1)
            print('Procesando Lista de la Matriz')
            for se in range(aux.devolver_tamano1()):
                try:
                    reb = int(aux.buscar_indice(se))
                    #print(reb)
                    bin = int(reb/reb)
                    #print(bin)
                    bina_aux.insertar(bin)
                except ZeroDivisionError:
                    bina_aux.insertar(0)
                #bina_aux.imprimir()
            bina.insertar(bina_aux)
            time.sleep(1)
            print('Calculando lista binaria')
        time.sleep(2)
        print('Matriz Binaria Lista'+'\n')

        tamano = bina.devolver_tamano()
        #bina.imprimir()
        #print('\n')
        respuesta = linked_list()
        respuestas = ''
        time.sleep(2)
        print('Realizando comparacion binaria')
        for mon in range(bina.devolver_tamano()):
            #respuesta = linked_list()
            contadores = -1
            contador_a += 1
            aux_lista = bina.buscar_indice(mon)
            f = 0
            # print(list)
            respuestas += '['
            #respuesta.borrar()
            for i in range(contador_a, tamano):
                # print(i)
                if i == (tamano - 1):
                    # print('No sale')
                    break
                else:
                    try:
                        if bina.buscar_indice(contador_a).string() == bina.buscar_indice(i+1).string():
                            #binario[contador] == binario[i + 1]:
                            #tuplado.append(binario[contador])
                            tuplada.insertar(bina.buscar_indice(contador_a))
                            #bina.eliminar_lista(bina.buscar_indice(i+1))
                            #bina.imprimir()
                            #print('TA WUENO')
                            #f += 1
                            contadores += 1
                            if contadores == 0:
                                #respuesta.insertar(101)
                                if respuesta.buscar_num(contador_a):
                                    if respuesta.buscar_num(i+1):
                                        continue
                                    else:
                                        respuesta.insertar(i+1)
                                        f += 1
                                        #respuestas += str(i + 1)
                                else:
                                    respuesta.insertar(contador_a)
                                    f += 1
                                    #respuestas += str(contador_a)
                                    if respuesta.buscar_num(i+1):
                                        continue
                                    else:
                                        respuesta.insertar(i+1)
                                        f += 1
                                        #respuestas += str(i + 1)
                                #respuesta.insertar(i+1)
                            else:
                                if respuesta.buscar_num(i+1):
                                    continue
                                else:
                                    respuesta.insertar(i+1)
                                    f += 1
                                    #respuestas += str(i+1)
                    except IndexError:
                        break

            #if respuesta.devolver_tamano1() != 0:
            #    coordenadas.insertar(respuesta)
            if f != 0:
                frecuencias.insertar(f)
                #frecuencias.imprimir()
        time.sleep(2)
        print('Similitudes encontradas')
        #print(respuesta.string())
        #print(frecuencias.string())
        reducida_aux = linked_list1()
        redux_2 = linked_list()
        #redux_1 = linked_list()
        time.sleep(2)
        print('Sumando tuplas identicas')
        contador_b = 0
        tams = frecuencias.devolver_tamano1()
        for asmnj in range(tams):
            muetsra = frecuencias.buscar_indice(asmnj)
            contador_sumas = 0
            #redux_1.borrar()
            redux_1 = linked_list()
            for asnmpp in range(contador_b, muetsra+contador_b):
                valor = 0
                contador_b += 1
                contador_sumas += 1
                posicion = respuesta.buscar_indice(asnmpp)
                #print(posicion)
                if contador_sumas == 1:
                    aux_red = self.linked_list1.buscar_indice(posicion)
                elif contador_sumas > 1:
                    aux_red_ant = self.linked_list1.buscar_indice(posicion)
                    if contador_sumas > 2:
                        aux_red.borrar()
                        for ja in range(redux_1.devolver_tamano1()):
                            aux_red.insertar(redux_1.buscar_indice(ja))
                        redux_1.borrar()
                    #print(aux_red_ant.devolver_tamano()+1)
                    for cai in range(aux_red_ant.devolver_tamano()+1):
                        #print(cai)
                        num_a = int(aux_red.buscar_indice(cai))
                        #print(aux_red.buscar_indice(cai))
                        num_b = int(aux_red_ant.buscar_indice(cai))
                        #print(aux_red_ant.buscar_indice(cai))
                        valor = int(num_a + num_b)
                        #print(valor)
                        redux_1.insertar(valor)
            #print(redux_1.string())
            reducida_aux.insertar(redux_1)
        time.sleep(2)
        print('Procesando sumas')
        #print(reducida_aux.string())
        cad = respuesta.string()
        for aqu in range(self.linked_list1.devolver_tamano()):
            numabus = aqu
            if cad.find(str(numabus)) > 0:
                continue
            else:
                #print('Perdido')
                reducida_aux.insertar(self.linked_list1.buscar_indice(numabus))
                #frecuencias.insertar(0)
        #print(frecuencias.string())
        #print(reducida_aux.string())
        #print(str(self.nombre)+' '
              #+str(reducida_aux.devolver_tamano())+' '
              #+str(str(self.m))+' '
              #+str(reducida_aux))
        time.sleep(2)
        print('Matriz reducida lista')
        print('\n')
        retorno_reducida = Matriz(str(self.nombre), reducida_aux.devolver_tamano(),
                                  self.m, reducida_aux)
        return (retorno_reducida, frecuencias)


    def grafico(self):
        cont = -1
        with open('grafos/grafo_'+str(self.nombre)+'.dot', 'w') as re:
            re.write('digraph G {' + '\n')
            re.write('splines="False";' + '\n')

            re.write('/* Entidades */' + '\n')
            re.write('Matriz [label="'+self.nombre+'", shape="oval"]' + '\n')
            re.write('N [label="n='+str(self.n)+'", shape="doublecircle", color="blue"]' + '\n')
            re.write('M [label="m='+str(self.m)+'", shape="doublecircle", color="blue"]' + '\n')

            re.write('/* Relaciones */' + '\n')
            re.write('Matriz -> N' + '\n')
            re.write('Matriz -> M' + '\n')

            cont1 = -1
            for sa in range(self.n):
                cont += 1
                aux = self.linked_list1.buscar_indice(sa)
                for se in range(self.m):
                    cont1 += 1
                    if cont == 0:
                        re.write(
                            'AUX' + str(cont1) + ' [label="' + str(aux.buscar_indice(se)) + '", shape="circle", '
                                                                                            'color="red"]' + '\n')
                        re.write('Matriz -> ' + 'AUX' + str(cont1) + '\n')
                    elif cont <= self.linked_list1.devolver_tamano():
                        anterior = aux.buscar_indice(cont - 1)
                        re.write(
                            'AUX' + str(cont1) + ' [label="' + str(aux.buscar_indice(se)) + '", shape="circle", '
                                                                                            'color="red"]' + '\n')
                        re.write('AUX' + str(cont1 - self.m) + ' -> ' + 'AUX' + str(cont1) + '\n')

            re.write('}')

            re.close()
        os.system('dot -Tpng ' + 'grafos/grafo_'+str(self.nombre)+'.dot' + ' -o grafos/imagen_'+str(self.nombre)+'.png')
        #webbrowser.open('grafos/imagen_'+str(self.nombre)+'.png')