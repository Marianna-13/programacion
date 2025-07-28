#append
#1
# numero=[]
# print (numero)
# num1=7
# numero.append(num1)
# print(numero)
#2
# nombres=[]
# print(nombres)
# nom1=("ana")
# nom2=("lucia")
# nom3=("carlos")
# nombres.append(nom1)
# nombres.append(nom2)
# nombres.append(nom3)
# print (nombres)

#insert
#1
# lista=[1,2,3]
# lista.insert(0, 99)
# print (lista)
#2
# lista=["azul","verde"]
# lista.insert(1,"rojo")
# print (lista)


#extend
#1
# numeros=[4,5,6]
# numeros.extend([1,2,3])
# print(numeros)
#2
# letras=["a","b","c"]
# letras.extend(["ok"])
# print(letras)

#Remove
#1
# frutas=["manzana","uva","pera"]
# frutas.remove("uva")
# print (frutas)
#2
# numeros=[1,2,3,2]
# numeros.remove(2)
# print(numeros)

#pop
#1
# lista=[1,2,3,4]
# valor=lista.pop(3)
# print(lista)
# print(valor)
#2
# numeros=["uno","dos","tres"]
# valor=numeros.pop(0)
# print (numeros)

#clear
#1
# lista=[1,2,3,4]
# lista.clear()
# print(lista)
#2
# elementos=[]
# ele1=input("ingrese el primer  elemento: ")
# ele2=input("ingrese el segundo  elemento: ")
# ele3=input("ingrese el tercer  elemento: ")
# ele4=input("ingrese el cuarto  elemento: ")
# ele5=input("ingrese el quinto  elemento: ")
# lista=[ele1,ele2,ele3,ele4,ele5]
# print (lista)
# lista.clear()
# print(lista)

#index
#1
# frutas=["manzana","uva","pera"]
# print(frutas)
# print (frutas.index("pera"))
#2
# numeros=[4,5,6,7]
# print(numeros)
# print (numeros.index(6))

#count
#1
# lista=[3,1,3,5,3]
# print (lista)
# print (lista.count(3))
#2
# letras=["a","b","a","c","a"]
# print (letras)
# print (letras.count("a"))

#sort
#1
# numeros=[5,1,4,2]
# numeros.sort()
# print (numeros)
# #2
# letras=["z", "a", "m", "b"]
# letras.sort()
# print(letras)

#reverse
#1
# numeros=[1,2,3,4]
# numeros.reverse()
# print(numeros)
# #2
# lista=["inicio","medio","fin"]
# lista.reverse()
# print(lista)

#copy
#1
# original=[1,2,3]
# nueva=original.copy()
# nueva.append(4)
# print(original)
# print(nueva)
#2
# lista_original=["a","b","c"]
# nueva=lista_original.copy()
# nueva.append("d")
# print(lista_original)
# print(nueva)

#Actividad de listas
lista1=[1,2,3,4,5]
lista2=[6,7,8,9,10]

lista1.append(100)
lista1.append("Hola Mundo")

lista2.append("Hola Y Adios")
lista2.append(300)

lista3=lista1.copy()
lista3.remove("Hola Mundo")
lista4=lista2.copy()
lista4.remove("Hola Y Adios")
lista4.remove(300)


lista5=[]
lista5.extend(lista4)
lista5.extend(lista3)

print("LISTA 1",lista1)
print("LISTA 2",lista2)
print("LISTA 3",lista3)
print("LISTA 4",lista4)
print("LISTA 5",lista4)

