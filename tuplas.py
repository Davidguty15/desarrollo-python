mi_tupla=()
mi_tupla=(1,2,3,4,5)
mi_tupla=(1,2,3,4,5)
mi_tupla=mi_tupla+(6,)
print(mi_tupla)
mi_tupla=mi_tupla+(7,)
print(mi_tupla)

mi_tupla=(1,2,3,4,5,6,7)
mi_lista=list(mi_tupla)
mi_lista.remove(1)
mi_tupla=tuple(mi_lista)
print(mi_tupla)

mi_tupla=(2,3,4,5,6,7)
mi_tupla=()
print(mi_tupla)

mi_tupla=(1,2,3,4,5,6,7)
print(len(mi_tupla))

mi_tupla=(1,2,3,4,5,6,7)
print(mi_tupla.count(8))

mi_tupla=(1,2,3,4,5,6,7)
print(mi_tupla.index(3))

mi_tupla=(1,2,3,4,5,6,7)
print(min(mi_tupla))

print(max(mi_tupla))

print(sum(mi_tupla))

mi_tupla2="mango","pera","uva"
print(type(mi_tupla2))

mi_tupla3=mi_tupla + mi_tupla2
print(mi_tupla3)

print(mi_tupla3[6:10])

tupla_4=(1,(2,3,4),5)
print(tupla_4)
print(tupla_4[1][1])
print(tupla_4[1][1:3])
print(tupla_4[1][1:3][0])

tupla_5=("mango","pera","uva")
print(tuple(tupla_5))

otra_tupla=tuple("mango")
print(type(otra_tupla))
print(otra_tupla)

