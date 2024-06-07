#declaramos una funcion
def suma(valor1, valor2):
    resultado = valor1 + valor2
    return resultado

#print(f"el resultado es : {suma(1,5)}" )
#esto es un array
numeros = [1,2,3,4]

#recorremos el array
for numero in numeros:
    print(f"ciclo for {numero}")
   
i = 0
while i < len(numeros):
    #print(f"ciclo while {numeros[i]}")
    i += 1

edad = 10

if edad >= 18:
    print("eres mayor de edad")
else:
    print("no eres mayor")

golesArgentina = 3
golesFrancia = 2

if golesArgentina > golesFrancia:
    print("gana Argentina")
elif golesFrancia > golesArgentina:
    print("gana Francia")
else:
    print("empate")


persona = {
    "nombre": "Fulano",
    "edad": "10",
    "ciudad": "vdr"
}

persona["nacionalidad"] = "Argentino"

print(f"El nombre es: {persona['nombre']}")
print(f"La edad es: {persona['edad']}")
print(f"La nacionalidad es: {persona['nacionalidad']}")

with open("mi.txt", "w") as archivo:
    archivo.write("hola mundo que tal como va todo")

with open("mi.txt", "r") as archivo:
    texto = archivo.read()
    print(f"El texto es: {texto}")

palabra = "mun"

with open("mi.txt", "r") as archivo:
    #lineas = []
    for linea in archivo:
        if palabra in linea:
            print(f"encontro: {palabra}" )
        else:
            print("error")

#fizz buzz
#si es multiplo de 3 -> fizz
#si es multiplo de 5 -> buzz
#si es multiplo de 3 y 5 -> fizzbuzz





for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
      






 





#variable = "un string"

#resultado = sum1 + sum2
#print(resultado)
#print(variable)

