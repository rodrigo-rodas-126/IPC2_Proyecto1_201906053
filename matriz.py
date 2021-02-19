from listacircular import ListaCiruclar
import webbrowser
from estructuras import linked_list1
from estructuras import linked_list
import os

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
        pass

    def suma(self):
        pass

    def grafico(self):
        cont = -1
        with open('grafo_'+str(self.nombre)+'.dot', 'w') as re:
            re.write('digraph G {' + '\n')
            re.write('splines="FALSE";' + '\n')

            re.write('/* Entidades */' + '\n')
            re.write('Matrizes [label="matrices", shape="oval"]' + '\n')
            re.write('Matriz [label="Ejemplo", shape="oval"]' + '\n')
            re.write('N [label="'+str(self.m)+'", shape="doublecircle", color="blue"]' + '\n')
            re.write('M [label="'+str(self.n)+'", shape="doublecircle", color="blue"]' + '\n')

            re.write('/* Relaciones */' + '\n')
            re.write('Matrizes -> Matriz' + '\n')
            re.write('Matriz -> N' + '\n')
            re.write('Matriz -> M' + '\n')

            cont1 = -1
            for sa in range(self.linked_list1.devolver_tamano()):
                cont += 1
                aux = self.linked_list1.buscar_indice(sa)
                for se in range(aux.devolver_tamano1()):
                    cont1 += 1
                    if cont == 0:
                        re.write(
                            'AUX' + str(cont1) + ' [label="' + str(aux.buscar_indice(se)) + '", shape="circle"]' + '\n')
                        re.write('Matriz -> ' + 'AUX' + str(cont1) + '\n')
                    elif cont <= self.linked_list1.devolver_tamano():
                        anterior = aux.buscar_indice(cont - 1)
                        re.write(
                            'AUX' + str(cont1) + ' [label="' + str(aux.buscar_indice(se)) + '", shape="circle"]' + '\n')
                        re.write('AUX' + str(cont1 - self.m) + ' -> ' + 'AUX' + str(cont1) + '\n')

            re.write('}')

            re.close()
        os.system('dot -Tpng ' + 'grafo_'+str(self.nombre)+'.dot' + ' -o imagen_'+str(self.nombre)+'.png')
        webbrowser.open('imagen_'+str(self.nombre)+'.png')