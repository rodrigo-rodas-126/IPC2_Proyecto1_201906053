from listacircular import ListaCiruclar
import os
class Matriz():

    def __init__(self, nombre, n, m, listas):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.listas = listas

    def imprimir(self):
        print('Nombre: '+str(self.nombre)+' '+', n: '+str(self.n)+' '+', m: '+str(self.m))
        for lista in self.listas:
            print(lista)

    def tuplas(self):
        pass

    def binario(self):
        pass

    def suma(self):
        pass

    def grafico(self):
        cont = -1
        with open('grafo.dot', 'w') as re:
            re.write('digraph G {' + '\n')
            re.write('splines="FALSE";' + '\n')

            re.write('/* Entidades */' + '\n')
            re.write('Matrizes [label="matrices", shape="oval"]' + '\n')
            re.write('Matriz [label="Ejemplo", shape="oval"]' + '\n')
            re.write('N [label="'+str(self.n)+'", shape="doublecircle", color="blue"]' + '\n')
            re.write('M [label="'+str(self.m)+'", shape="doublecircle", color="blue"]' + '\n')

            re.write('/* Relaciones */' + '\n')
            re.write('Matrizes -> Matriz' + '\n')
            re.write('Matriz -> N' + '\n')
            re.write('Matriz -> M' + '\n')

            cont1 = -1
            for lista in self.listas:
                cont += 1
                for valor in lista:
                    cont1 += 1
                    if cont == 0:
                        re.write('AUX' + str(cont1) + ' [label="' + str(valor) + '", shape="circle"]' + '\n')
                        re.write('Matriz -> ' + 'AUX' + str(cont1) + '\n')
                    elif cont <= len(self.listas):
                        anterior = self.listas[cont - 1]
                        re.write('AUX' + str(cont1) + ' [label="' + str(valor) + '", shape="circle"]' + '\n')
                        re.write('AUX' + str(cont1 - self.m) + ' -> ' + 'AUX' + str(cont1) + '\n')

            re.write('}')

            re.close()
        os.system('dot -Tpng grafo.dot -o imagen1.png')