#Este espacio es para hablar de listas

#Crear una lista con los meses del año

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
#Imprimir la lista de meses
print(meses)
#Imprimir el primer mes de la lista
print(meses[0])
#Imprimir el último mes de la lista
print(meses[-1])
#Imprimir el tercer mes de la lista
print(meses[2])
#Imprimir el primer y segundo mes de la lista
print(meses[0:2])
#Imprimir el primer y segundo mes de la lista (otra forma)
print(meses[:2])
#Agregar un dia de la semana a la lista de meses
meses.append("lunes")
#Imprimir la lista de meses
print(meses)
#Eliminar el primer mes de la lista
meses.pop(0)
#Imprimir la lista de meses
print(meses)

#borrar todos los elementos de la lista
meses.clear()
#Imprimir la lista de meses
print(meses)

#eliminar la lista de meses

del meses

meses = []

meses.append("enero")
print(meses)

