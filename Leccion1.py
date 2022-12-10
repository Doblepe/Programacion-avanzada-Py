#tipos de datos complejos

#set 
#los elementos de un et son únicos (no se pueden repetir)
#los set son desordenados (no mantienen el orden con el que son declarados)
#sus elementos deben de ser inmutables
'''
miconjunto1  = set([3,2,1,4])
print(miconjunto1)
print(type(miconjunto1))

miconjunto2 = {3,2,1,1,3,4,8}
print(miconjunto2)
print(type(miconjunto2))

#operaciones
#miconjunto[2] = 3
#print(miconjunto[2])

for aux in miconjunto2:
    print(aux)

print( 1 in miconjunto2)

print(miconjunto1 | miconjunto2)

#métodos asociados

#añadir valor
miconjunto1.add(2)

#eliminar un elemento
miconjunto1.remove(2) #se le pasa el elemento que se quiere borrar y no el indice, si no exite dara error

#eliminar un elemento
miconjunto1.discard(2) #se le pasa el elemento que se quiere borrar y no el indice, si no exite No dara error

#eliminar un elemento aleatoriamente
miconjunto1.pop()

#elimina todos los elementos del conjunto
miconjunto1.clear()

#Otros Metodos
print(miconjunto1.union(miconjunto2))
print(miconjunto1.intersection(miconjunto2))
'''
'''
s1.union(s2[, s3 ...])
s1.intersection(s2[, s3 ...])
s1.difference(s2[, s3 ...])
s1.symmetric_difference(s2)
s1.isdisjoint(s2)
s1.issubset(s2)
s1.issuperset(s2)
s1.update(s2[, s3 ...])
s1.intersection_update(s2[, s3 ...])
s1.difference_update(s2[, s3 ...])
s1.symmetric_difference_update(s2)

'''

#tuplas

#son inmutables ( no se pueden modificar una vez declaradas)
from pickle import TRUE



mitupla = (1,23,5,3,1,(2,99))


print(mitupla)
print(type(mitupla))

#mitupla[2]=2 Error


print(mitupla[5][1])

for aux in mitupla:
    print(aux)


mitupla2 = (1,2,4,1)

x,y,z,u = mitupla2

#métodos
#contar el número que el elemento pasado por argumento aparece en la tupla
print(mitupla2.count(4))

#buscar el elemento que se le pasa como parámetro
print(mitupla2.index(1)) #si no exite devuelve error

print("#########")
print(mitupla2.index(1,2)) #acepta un segunda parámetro que será el indice desde donde comience a contar 


#como contar los elementos no duplicados de una tupla

len(set(mitupla2))

#lista
#son ordenadas
#acepta cualquier tipo de dato
#pueden ser indexadas
#se pueden anidar
#son mutables y dinámicas 

lista1 = [1,2,3,4]

lista2 = list("123")
print(lista2)


print(lista1[2])
print(lista1[-1])
#print(lista1[-3:])
#print(lista1[-3:])
#print(lista1[:3])

milista3 = [1,2,3,['a',TRUE,2,[4,3,99]]]

print(milista3[3][3][2])

#lista1 += lista2

print(lista1)

for aux in lista1:
    print(aux)
    

#crear las tablas de multiplicar mediante listas

tabla_desde = 1 #tablas del 1...
tabla_hasta = 10 #...al 10
desde = 1 #multiplicaciones desde el 1...
hasta = 10 #...hasta el 10

for factor1 in range(tabla_desde, tabla_hasta + 1):
	print(f'Tabla de multiplicar del {factor1}:') #mostramos una cabecera para cada tabla
	for factor2 in range(desde, hasta + 1):
		print(f'{factor1} x {factor2} = {factor1 * factor2}')
	print() #línea en blanco al final de cada tabla


lista1 = list()
lista2 = list()
for i in range(11):
    lista1.append(i)
    lista2.append(i)      
    
for i in lista1:
    for j in lista2:
        print(str(i) + 'x' + str(j) + '=' + str(i*j))  
        
'''
0x1=0
...
0x10=0

1x1=1
...
10x10=100
'''

#métodos
#añadir elemento
lista1.append(2)

#añadir/extender una lista dentro de entro
lista1.extend([2,3,5])

#insertar un elemento en un posición determinada
lista1.insert(1,2)#insert(<index>, <obj>)

#eliminar un elemento 
lista1.remove(2) #si no existe el elemento nos da error

#eliminar el último elemento
lista1.pop()

#invertir el órden de la lista
lista1.reverse()

#ordenar la lista
lista1.sort(reverse=True)

#nos devuelve el indice desde su primera ocurrencia
lista1.index(2)

lista1.index(2,4) #index(<obj>[,index])



#diccionarios
#son dinámicos, pueden varias su tamaño
#son indexados, podemos acceder a traves de la key
#son anidados,


d1 = {
    "nombre":"Luis",
    "edad":30
}

d2 = dict ([
    ('nombre','Luis'),
    ('edad',30)
    ])


print(d1['edad'])
print(d1.get('nombre'))

d1['nombre'] = 'Luisa'
print(d1)

for x in d1:
    print(x) #recorre las claves
 
print("#####")   
for x in d1:
    print(d1[x])
    

for x,y in d1.items():
    print(x,y)

#diccionario anidado    
d1_anidados = {"a":1,"b":2}
d2_anidados = {"a":1,"b":2}

d3 = {
    "d1":d1_anidados,
    "d2":d2_anidados
}
print(d3)

#métodos 

#Eliminar todo el contenido
d1.clear()

#consultar un valor mediante una key
#get(<key>,[valor por defecto])

print(d2.get("nombre2","No encontrado"))

#devolver un listado con las keys y values
it = d2.items()
print(it)
print(list(it))

#obtener todas las keys
print(list(d2.keys()))

#obtener todos los valores
print(list(d2.values()))

#buscar y eliminar un registro mediante su key
#d2.pop("nombre2") #si no queremos que nos devuelve error en el caso de que la key no exista, añadimos un segundo parametro
d2.pop("nombre2",-1)
print(d2)

#elimina de forma aleatoria un item
d2.popitem()

#actualizar los values si hay match con alguna key y si no ayude un nuevo registro

d1_anidados = {"a":1,"b":2}
d2_anidados = {"a":4,"c":2}

d1_anidados.update(d2_anidados)
print(d1_anidados)

#ejemplo
my_carrito = ["platanos","platanos","naranjas"]

stock = {
    "platanos":4,
    "naranjas":10,
    "manzanas":8
}

precios = {
    "platanos":0.2,
    "naranjas":0.05,
    "manzanas":0.1
}

def pasar_por_cajar(lista_compra):
    total_a_pagar=0
    for elemento in lista_compra:
        precio = precios[elemento]
        if stock[elemento] > 0:
            total_a_pagar += precio
            stock[elemento] -= 1
    
    return total_a_pagar

salida = pasar_por_cajar(my_carrito)

print(salida)
print(stock)
#Realiza una calculadora
rango = range(11)
rango = list(rango)  
for num in rango:
    print(f'{num} por {rango[num]} = {rango[num] * num}')
