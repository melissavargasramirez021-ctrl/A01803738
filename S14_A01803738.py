# este es un codigo que fevisa si eres adulto o no 

edad=int(input("cuantos años tienes?"))

if edad >= 18:
    print("eres adulto")
else:
    print("no eres adulto") 



# este codigo revisa si eres adolescente 

edad = int(input("cuantos años tienes? "))
if edad >= 13 and edad <= 19:
  print("eres adolescente")
else:
  print("no eres adolescente")



# este es un codigo que calcula tu edad con tu año de nacimiento 

nacimiento = int(input("en que año naciste?"))
año_actual = 2025
edad = año_actual-nacimiento
print("tienes", edad, "años") 

