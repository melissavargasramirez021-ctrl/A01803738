donas = int(input("ingresa la cantidad de donas: ")) 
docenas = donas // 12 
print("con", donas, "donas puedes hacer", docenas, "docenas")

num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: ")) 
residuo = num1 % num2print(num1, "dividido entre", num2, "tiene un residuo de", residuo) 

segundos = int(input("ingresa una cantidad de segundos:"))
horas = segundos // 3600 minutos = (segundos % 3600) // 60 
seg_restantes = segundos % 60
print(segundos,"segundos son",horas,"horas,",minutos,"minutos y",seg_restantes,"segundos")
