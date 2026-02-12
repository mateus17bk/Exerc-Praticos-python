#1)Faça um algoritmo que leia um número e mostre se o mesmo é positivo, negativo ou zero.
num = float(input("Digite o número: "))
if (num > 0):
    print("O número é positivo.")
elif (num < 0):
    print("O número é negativo.")  
else:
    print("O número é zero.")

#2) Faça um algoritmo que leia um número e mostre se o mesmo é par ou ímpar.
num = float(input("Digite o número: "))
if(num % 2 == 0):
    print("O número é par.")
else:
    print("O número é ímpar.")

#3) Faça um algoritmo que leia dois números e imprima o maior.
num1 = float(input("Informe o primerio número: "))
num2 = float(input("Informe o segundo número: "))
if(num1 > num2):
  print("O primeiro número é maior.")
else:
  print("O segundo número é maior.")
