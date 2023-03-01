from functools import reduce
lista = [1,2,3,4,5,6]
resultado = filter(lambda x:x%2 != 0,lista)
def suma(a,b):
    return a+b
res = reduce(suma, resultado)
print(res)