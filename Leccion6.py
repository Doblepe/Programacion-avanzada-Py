#fichero = open('test.txt', 'a')
# print(fichero.read())
# lineas = fichero.readlines()
# #print(lineas)
# for l in lineas:
#     print(l)

# with open('test.txt') as fichero:
#     lineas = fichero.readlines()

#print(lineas)
open('mytest.txt',)
with open('test.txt', 'w') as fichero:
    lista = ('1','2','3')
    for l in lista:
        fichero.writelines(l + '\n')
# fichero.write('Aquí he venido porque aquí estoy')
# fichero.close()
