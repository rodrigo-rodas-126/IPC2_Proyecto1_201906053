from nodo import Nodo

class ListaCiruclar():

  def __init__(self):
    self.first = None
    self.last = None

  def Vacia(self):
    return self.first == None

  def AgregarInicio(self, dato):
    if self.Vacia():
      self.first = self.last = Nodo(dato)
      self.last.next = self.first
    else:
      aux = Nodo(dato)
      aux.next = self.first
      self.first = aux
      self.last.next = self.first

  def AgregarFinal(self,dato):
    if self.Vacia():
      self.first = self.last = Nodo(dato)
      self.last.next = self.first
    else:
      aux = self.last
      self.last = aux.next = Nodo(dato)
      self.last.next = self.first

  def Recorrer(self):
    aux = self.first
    while aux.next != self.first:
      print(aux.dato)
      aux = aux.next
    print(aux.dato)