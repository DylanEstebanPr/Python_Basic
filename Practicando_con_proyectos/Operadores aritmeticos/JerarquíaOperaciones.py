#La jerarquia es el orden de operaciones
num1 = 100
num2 = 50
num3 = 25
num4 = 30

print(num1 + num2 * num3)
print((num1 + num2) * num3) #Aqui la jerarquia se resuelve primero lo del parentesis es decir la suma y despues la multiplicacion distinto a lo de arriba

print((num1 + num2) * (num3 - num4)) #En este caso se resuelven primero lo que está en los parentesis y de ultimas la multiplicación

