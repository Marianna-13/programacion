#SENTENCIA ELIF
# letras=input("Ingrese las vocales: ")
# palabras=""
# if letras.lower():
#      palabras +=letras.lower()
# elif letras.lower():
#      palabras+=letras
# else:
#      palabras+=letras xxxxxxxxxxxxxxxxxxxxxx

#Ejercicios con condicionales y operaciones matematicas
#1. verifica si un numero es positivo negativo o cero
# numero=int(input("Ingresa un numero: "))
# if numero >1:
#     print("El numero es positivo")
# elif numero <-1:
#     print("El numero es negativo")
# else:
#     print("El numero es cero")

#2. calcula el mayor de dos numeros ingresados
# num1=int(input("Ingresa el primer  numero: "))
# num2=int(input("Ingresa el segundo  numero: "))
# if num1 > num2:
#     print("El primer numero es mayor")
# elif num1 < num2:
#     print("El segundo numero es mayor")
# else:
#     print("Los numeros son iguales")

#3. Determina si un numero es par o impar
# numero=int(input("Ingresa un numero: "))
# if numero % 2==0:
#     print("El numero es par")
# else:
#     print("El numero es impar")

#4.Dado un numero, verifica si esta entre 10 y 20.
# numero=int(input("Ingresa un numero: "))
# if numero >=10 and numero <=20:
#     print("El numero SI esta entre 10 y 20")
# else:
#     print("El numero NO esta entre los dos numeros dados")


#5. Dados tres numeros, encuentra el mayor usando condicionales.
# num1=int(input("Ingresa un numero: "))
# num2=int(input("Ingresa un numero: "))
# num3=int(input("Ingresa un numero: "))
# if num1>= num2 and num1>=num3:
#     print("El numero mayor es ",num1)
# elif num2>=num1 and num2>=num3:
#     print("El numero menor es ",num2)
# else:
#     print("El mayor es ",num3)


#6. Calcula el precio final con un 10% de descuento si el total es mayor a $100.
# precio=float(input("Ingresa el precio de tu compra: "))
# if precio >=100:
#     descuento=precio*0.10
#     precio_F=precio-descuento
#     print("A su compra se le aplico un 10% de descuento, su precio final es ",precio_F)
# else:
#     print("A su compra no se le aplico el descuento, el precio final es: ",precio)


#7. Verifica si una persona puede votar (mayor o igual a 18).
# edad=int(input("Ingresa tu edad: "))
# if edad >=18:
#     print("Puede votar")
# else:
#     print("No puede votar")


#8. Dado el precio y tipo de cliente (VIP o normal), aplica un descuento del 20% solo a VIP.
# precio=float(input("Ingresa el precio de tu compra: "))
# tipo_de_cliente=input("Que tipo de cliente eres (VIP o normal): ")
# if tipo_de_cliente == "VIP":
#     descuento=precio*0.20
#     precio_final=precio-descuento
#     print("Por ser cliente VIP, se te aplicara el 20 de descuento, por lo tanto tu precio final sera ",precio_final)
# else:
#     print("No se te aplicara descuento, por lo tanto tu precio final es ",precio)


#9.Determina si un numero es multiplo de 5 y de 3 al mismo tiempo
# numero=int(input("Ingrese un numero "))
# if numero % 5 == 0 and numero % 3 == 0:
#     print("El numero es multiplo de 5 y de 3 al mismo tiempo")
# else:
#     print("El numero no es multiplo de ninguno de los dos numeros dados")


#10. Dado un numero, verifica si es divisible entre dos numeros dados.
# numero=int(input("Ingresa un numero "))
# if numero % 2 == 0:
#     print("El numero SI es divisible entre dos")
# else:
#     print("El numero NO es divisible entre dos")


#11. Crea una lista con 5 numeros . si el tercer numero es mayor que 10, muestra "Mayor a diez", si no, muestra "Menor o igual a 10"
# num1=int(input("Ingresa el primer  numero: "))
# num2=int(input("Ingresa el segundo numero: "))
# num3=int(input("Ingresa el tercer  numero: "))
# num4=int(input("Ingresa el cuarto  numero: "))
# num5=int(input("Ingresa el quinto  numero: "))
# numeros=[num1,num2,num3,num4,num5]



#18. Convierte la tupla (1, 2, 3) a lista, cambia el segundo valor a 10 solo si es igual a 2, luego vuelve a convertirla en tupla y muéstrala.
numeros=(1, 2, 3)
lista=list(numeros)
print(lista)
if lista [1] == 2:
     lista[1]=10
     numeros=tuple(lista)
     print("Tupla actualizada",numeros)
else:
     print("Los numeros o son correctos")
