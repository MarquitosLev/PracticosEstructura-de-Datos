from deque import Deque

col = Deque()
col.add_last(12)
col.add_last("Hola")
col.add_last("First")
col.add_last(10)
print(col)

col.delete_last()
print(col)
print(col._size)

col.delete_first()
print(col)
print(col._size)

col.add_first("Hola")
col.add_first("Puto")
print(col)
print(col._size)