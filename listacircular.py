from nodo import Nodo

class ListaCiruclar():

  def __init__(self):
    self.first = None
    self.last = None

  def Vacia(self):
    return self.first == None

  def AgregarInicio(self, Matriz):
    if self.Vacia():
      self.first = self.last = Nodo(Matriz)
      self.last.next = self.first
    else:
      aux = Nodo(Matriz)
      aux.next = self.first
      self.first = aux
      self.last.next = self.first

  def AgregarFinal(self,Matriz):
    if self.Vacia():
      self.first = self.last = Nodo(Matriz)
      self.last.next = self.first
    else:
      aux = self.last
      self.last = aux.next = Nodo(Matriz)
      self.last.next = self.first

  def Recorrer(self):
    aux = self.first
    while aux.next != self.first:
      print(aux.Matriz.nombre)
      aux = aux.next
    print(aux.Matriz.nombre)

  def Listar(self, nom_matr):
    cont_maz = -1
    aux = self.first
    if aux.Matriz.nombre == nom_matr:
      return self.first.Matriz
    else:
      while aux.next.Matriz.nombre != nom_matr:
        cont_maz += 1
        #print(aux.dato)
        aux = aux.next
      return aux.Matriz
