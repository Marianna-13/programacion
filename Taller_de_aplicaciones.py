#Ejercicios de aplicaciones

#Calculadora de promedio
# lista=[]
# nota1=float(input("Ingrese la primera nota: "))
# nota2=float(input("Ingrese la segunda nota: "))
# nota3=float(input("Ingrese la tercera nota: "))
# suma=nota1+nota2+nota3
# promedio=suma/3
# lista.append(nota1)
# lista.append(nota2)
# lista.append(nota3)
# print(f"El promedio y la lista son: {promedio}, {lista}")

#Actualiza productos
# productos={"manzana":2.200,
#            "huevos":1.000,
#            "queso":5.000
# }
# print(productos)
# porcentaje=float(input("porcetaje de aumento (%): "))
# productos["manzana"]+=productos["manzana"]*(porcentaje/100)
# productos["huevos"]+=productos["huevos"]*(porcentaje/160)
# productos["queso"]+=productos["queso"]*(porcentaje/100)
# print(productos)

#conversor de temperaturas
# tem1=float(input("Ingerese la primera temperatura: "))
# tem2=float(input("Ingrese la segunda temperatura: "))
# tem3=float(input("Ingrese la tercer temperatura: "))
# tem4=float(input("Ingrese la cuarta temperatura: "))
# tem5=float(input("Ingrese la quinta temperatura: "))
# celcius=[tem1,tem2,tem3,tem4,tem5]

# f1=tem1*9/5+32
# f2=tem2*9/5+32
# f3=tem3*9/5+32
# f4=tem4*9/5+32
# f5=tem5*9/5+32
# fahrenheit=(f1,f2,f3,f4,f5)

# print(f"La temperatur en celcius es {celcius}")
# print(f"La temperatura en fahrenheit es {fahrenheit}")

#Edad promedio con listas
# edades=[int(input("edad1: ")),int(input("edad 2: ")),int(input("edad 3: ")),int(input("edad 4: ")),int(input("edad 5: "))]
# promedio=sum(edades)/len(edades)
# print(f"mayor: {max(edades)}, menor: {min(edades)}, promedio: {promedio}")

#Diccionario de frutas
# frutas={"manzana":2.500,
#         "banana":1.500,
#         "naranja":2.400
#         }
# p1=float(input("Cuantos kilos quiere de manzana: "))
# p2=float(input("Cuantos kilos quiere de banana: "))
# p3=float(input("Cuantos kilos quiere de naranja: "))
# cantidad_kilos1=p1*frutas["manzana"]
# cantidad_kilos2=p2*frutas["banana"]
# cantidad_kilos3=p3*frutas["naranja"]
# total=cantidad_kilos1+cantidad_kilos2+cantidad_kilos3
# print(f"El total de la manzana es {cantidad_kilos1}, el de la banana es {cantidad_kilos2}, el de la naranja es {cantidad_kilos3},y el total de los tres productos es {total}")

#Suma de elemtos en tupla
numeros=(1,2,3,4,5)
tupla=list(numeros)
lista=tuple(tupla)
print(lista)