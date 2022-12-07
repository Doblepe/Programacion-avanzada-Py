#Cómo obtener el valor máximo de una lista sin usar la función max()
lista = [1,44,36,26,255,36,66,7,2,77,1234]
lista.sort(reverse=True)

print(lista[0])
#Eliminar los duplicados
lista = set(lista)
print(lista)

