from dato import Dato

class Cola:
  def __init__(self):
    self.cola = []

  def encolar(self, Dato):
    self.cola.append(Dato)

  def devolver_tamano(self):
    return len(self.cola)

  def imprimir(self):
    for elemento in self.cola:
      print(elemento.valor, end=" <= ")

  def desencolar(self):
    if self.cola:
      ff = self.cola.pop(0)
      return ff

