from datos.clientes import Persona
from datos.clientes import Cliente

cliente1 = Cliente("Adam", "Jakob", 32, "ajakob@gmail.com", 236541, "B", 40.000)

cliente2 = Cliente("Nicolas", "Pinot", 30, "npintot@gmail.com", 987456, "A", 62.000)


print(cliente1)

print(cliente1.aprobar_credito())
print("========================")


print(cliente2)

print(cliente2.aprobar_credito())
