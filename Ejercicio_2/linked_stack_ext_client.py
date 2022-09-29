from LinkedStackExt import LinkedStackExt
from LinkedStack import LinkedStack

#Creacion de pila e ingreso de elementos a la pila
pila = LinkedStackExt()
pila.push("Primer ingresado")
pila.push("Hola")
pila.push(99)
pila.push(12.5)
pila.push("Marcos")
pila.push("Gosti")
pila.push("Ricardo")
pila.push("Santu")
pila.push(666)
pila.push("Tope")
print(pila)

#Prueba de metodo multipop, quitar despues
print("Elementos Eliminados: ", pila.multi_pop(5))
print(pila)

#Prueba metodo exchange
pila.exchange()
print(pila)

