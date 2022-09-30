from LinkedStackExt import LinkedStackExt
from LinkedStack import LinkedStack

#Creacion de pila e ingreso de elementos a la pila
pila = LinkedStackExt()
pila.push("Primero")
pila.push("Wiccan")
pila.push(99)
pila.push(12.5)
pila.push("Star-Lord")
pila.push("Python")
pila.push(33)
pila.push(10.1)
pila.push("Super")
pila.push(666)
pila.push("Tope")

print(pila)

# Prueba de metodo multipop
print("\nPrueba de metodo multipop")
print("Elementos Eliminados: ", pila.multi_pop(5))
print(pila)

# Prueba de metodo replace_all
print("\nPrueba de metodo replace_all: Wiccan -> Speed")
pila.replace_all("Wiccan", "Speed")
print(pila)

# Prueba metodo exchange
print("\nPrueba de metodo exchange")
pila.exchange()
print(pila)

