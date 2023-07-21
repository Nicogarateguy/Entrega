class Persona:
  def __init__(self, n, a, e, m, t):
    self.nombre = n
    self.apellido = a
    self.edad = e
    self.mail = m
    self.telefono = t

  def __str__(self):
        pass  
  
class Cliente(Persona):
  def __init__(self, n, a, e, m, t, c, s):
    super().__init__(n, a, e, m, t,)
    self.categoria = c 
    self.salario = s 

  def __str__(self):
        nombre = f"Nombre: {self.nombre} {self.apellido}\nCliente de categoria {self.categoria}"
        return nombre 
  
  def aprobar_credito(self):
     if self.categoria == "A" and self.salario > 60.000:
        return "Credito aprobado"
     else:
        return "Credito no aprobado"
     