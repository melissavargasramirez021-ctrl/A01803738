temp = [15, 15, 17, 30, 25, 30, 30, 31, 32, 30, 29]
media = sum(temp) / len(temp) 

print("temperatura promedio:", media)
for i in te,p: 
    if i > media: 
        print(i, "arriba de la media")
    elif i < media: 
      print(i, "anajo de la media")
    else:
      print(i, "igual a la media")

#ejercico 1: temoeraturas 
temp = [15, 17, 20, 25, 30, 28, 22]
media = sum(temp) / len(temp) 

print("temperatura promedio:", media) 
for t in temp: 
    if t > media: 
        print(t, "arriba de la media")
    elif t < media: 
        print(t, "abajo de la media") 
    else: 
        print(t, "igual a la media")

  # Ejercicio 2: dinero de dos personas 
persona1 = [200, 150, 300]
persona2 = [100, 250, 50] 

total1 = sum(persona1) 
total2 = sum(persona2) 
total_general = total1 + total2

print("total persona 1:", total1) 
print("total persona 2:", total2) 
print("total general:", total_general) 

#porcentaje de aporte 
print("porcentaje persona 1:", (total1 / total_general) * 100, "%") 
print("porcentaje persona 2:", (total2 / total_general) * 100, "%") 

#lista de compras 
compras = ["leche", "pan", "huevo ", "fruta", "arroz"]
hechas = []
no_hechas = []

for item in compras: 
        resp = input(f"¿ya compraste {item}? (si/no):").strip().lower()
        if resp == "si":
            hechas.append(item)
        else:
            no_hechas.append(item)
print("\ncompras hechas:", hechas) 
print("compras pendientes:", no_hechas) 

 
  
  #numeros de una lista 
  numeros = [15, 8, 30, 2, 50, 7, 20] 
print("lista original:", numeros) 
print("valor maximo:", max(numeros))
print("valor minimo:", min(numeros))
print(lista ordenada:", sorted(numeros))



# numeros pares e impares 
numeros = [10, 21, 32, 43, 54, 65, 76, 87] 

pares = [] 
impares = []
for n in numeros: 
    if n % 2 = = 0:
            pates.append(n)
        else:
            impares.append(n)
print("numeros pares:",pares)
pring("numeros impares:",impares)


# nombre de usuario 
usuario = []
while true: 
    nombre = input("ingresa un nombre de usuario (o 'fin' para terminar):")

    if nombre.lower() == "fin":
        break
    if nombre in usuarios: 
        print("ese nombre ya existe, elige otro.")
    else: 
        usuario.append(nombre)
print("lista final de usuarios:", usuarios) 

  





           
