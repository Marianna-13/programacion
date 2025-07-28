#CONDICIONALES, INTERACION Y ESTRUCTURAS DE DATOS
#1
# edad=int(input("¿Cuantos años tienes?: "))
# mensaje={
#     "menor":"Eres menor de edad",
#     "adulto":"Eres mayor de edad",
#     "adulto_mayor":"Eres adulto mayor"
# }
# if edad <18:
#     print(mensaje["menor"])
# elif edad >65:
#     print(mensaje["adulto_mayor"])
# else:
#     print(mensaje["adulto"])


#2
# estatura=float(input("Ingresa tu estatura en metros: "))
# if estatura < 1.5:
#     print("Tu estaura es baja")
# elif estatura <= 1.8:
#     print("Eres estatura media")
# else:
#     print("Eres alto")


#3
# numero=int(input("Ingresa un numero: "))
# if numero %2 == 0:
#     print("Es multiplo de 2")
# elif numero % 3 == 0:
#     print("Es multiplo de 3")
# else:
#     print("No es multiplo de 2 ni de 3")


#4
# numero=float(input("Ingresa un nunmero: "))
# numeroE, numeroD=str(numero).split(".")
# cantidad_decimales=len(numeroD)
# if cantidad_decimales == 1:
#     print("El numero tiene un decimal")
# elif cantidad_decimales == 2:
#     print("El numero tiene dos decimales")
# else:
#     print("El numero tiene mas de 2 decimales")


#5
# paises=("Colombia", "Peru", "Argentina", "Mexico")
# pais=input("Ingresa un pais: ")
# if pais in paises:
#     print("El pais si esta en la lista")
# else:
#     print("El pais no esta en la lista")


#6
# compatibilidad={
#  "A":["A","AB"],
#  "B":["B","AB"],
#  "AB":["AB"],
#  "O":["A","B","AB","O"]   
# }

# sangre=input("ingresa tu tipo de sangre (A, B, AB, O): ").upper()
# if sangre in compatibilidad:
#     print(compatibilidad[sangre])
# else:
#     print("Tu tipo de sangre no es compatible")


#7
# temperatura=float(input("Ingresa una temperatura en °c: "))
# if temperatura <10:
#     print("Hace frio")
# elif temperatura <= 25:
#     print("Esta templado")
# else:
#     print("Hace calor")


#8
# print("Menu de opciones ")
# print("1. suma")
# print("2. resta")
# print("3. multiplicacion")

# opcion=int(input("Elige una opcion (1, 2, 3): "))

# num1=int(input("Ingresa el primer numero: "))
# num2=int(input("Ingresa el segundo numero: "))

# if opcion == "1":
#     operacion=num1+num2
#     print(f"El resultado de la suma es ",{operacion})
# elif opcion == "2":
#     operacion=num1-num2
#     print(f"El resultado de la resta es {operacion}")
# elif opcion == "3":
#     operacion=num1*num2
#     print(f"El resultado de la multiplicacion es {operacion}")
# else:
#     print("La opcion o numero no son validas")xxxxxxxxxxxxxxxxxxxxxxxxxxx



#9
# meses={
#     1:"Enero",
#     2:"Febrero",
#     3:"Marzo",
#     4:"Abril",
#     5:"Mayo",
#     6:"Junio",
#     7:"Julio",
#     8:"Agosto",
#     9:"Septiembre",
#     10:"Octubre",
#     11:"Noviembre",
#     12:"Diciembre"
# }
# numero=int(input("Ingresa un numero del 1 al 12: "))
# if numero in meses:
#     print("El numero corresponde al mes de:",meses[numero])
# else:
#     print("El numero no esta entre 1 y 12, Intentao de nuevo")



#10
# numero=int(input("Ingresa un numero de cuatro dijitos: "))
# if numero == "1":
#     print("El numero empieza por 1")
# elif numero == "2":
#     print("El numero empieza por 2")
# else:
#     print("El numero empieza por otro digito")xxxxxxxxxxxxxxxxxxxxx


#11
# palabra=input("Ingresa una palabra: ")
# letra=palabra[0]
 
# vocales = "aeiouAEIOU"
# numeros = "0123456789"

# if letra in vocales: 
#  print("Empieza con vocal")
# elif letra in numeros: 
#  print("Empieza con un numero")
# else: 
#  print("Empieza con una consonante")


 #12
# print("Lista de frutas [manzana,pera,piña]")
# fruta=input("Ingresa un fruta: ")
# if fruta == "manzana":
#     print("Su precio es $1.000")
# elif fruta == "pera":
#     print("Su precio es $3.500")
# elif fruta == "piña":
#     print("Su precio es $ 2.200")
# else:
#     print("No esta disponible")


#13
# calificacion=float(input("Ingresa la calificacion (0 a 5): "))
# if calificacion <3:
#     print("Reprobado")
# elif calificacion <4:
#     print("Aprobado")
# else:
#     print("Exelente")


#14
# numero=float(input("Ingresa un numero: "))
# if numero % 4 == 0:
#     print("Es divisible entre 4")
# elif numero % 6 == 0:
#     print("Es divisible entre 6")
# else:
#     print("No es divisible enntre 4 y 6")


#15
# usuarios={
#     "felipe":"123",
#     "sonia":"abc",
#     "carlos":"animal"
# }
# usuario=input("Ingresa el usuarios: ")
# clave=int(input("Ingresa la clave: "))

# if clave == usuarios[usuario] :
#     print("Acceso permitido")
# else:
#     print("Acceso denegado")xxxxxxxxxxxxxxxxx


#16
# edad=int(input("Ingresa tu edad: "))

# if edad <12:
#     print("Eres un niño")
# elif edad < 17:
#     print("Eres un adolecente")
# elif edad < 64:
#     print("Eres un adulto")
# else:
#     print("Eres mayor")


#17
# capitales=("tirana","berlin","luanda","argel","riad")
# ciudad=input("Ingresa una ciudad ")
# if ciudad in capitales:
#     print(f"{ciudad} es una capital")
# else:
#     print(f"{ciudad} es una ciudad secundaria")


#18
valor=float(input("Ingresa el vaor de la compra: "))
if valor >200000:
    descuento=0.15
    valorF=valor*(1-descuento)
    print(f"Se aplico un 15% de descuento, valor final {valorF}")
elif 1000000<=valor<=2000000:
    descuento=0.10
    valorF=valor*(1-descuento)
    
