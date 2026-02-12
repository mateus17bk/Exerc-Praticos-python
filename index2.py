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

#4) Faça um algoritmo que peça a idade de uma pessoa e imprima na tela se a mesma já é maior de idade ou então, se a mesma é de menor.
idade = int(input("Informe a sua idade: "))
if(idade >= 18):
    print("Você é maior de 18 anos")
else:
    print("Você é menor de 18 anos")

# 5) Faça um algoritmo que peça a idade do usuário e a idade da sua mãe. Em seguida, imprima na tela com quantos anos sua mãe o teve.
minha_idade = int(input("Informe a sua idade: "))
mae_idade = int(input("Informe a idade a sua mãe: "))
result = (minha_idade - mae_idade)
if result < 0:
    print("Sua mãe te teve com:", abs(result))

# 6) Faça um algoritmo que imprima 50 vezes o caractere "-" na tela (sem a utilização de laços de repetição).
print(50 * "-")


# 7) Faça um algoritmo que verifica se um determinado valor é um número inteiro.
num = float(input("Digite o número: "))
if(num % 1 == 0):
    print("O número é inteiro")
else:    
    print("O número fracionário")

#8) Faça um algoritmo que verifica se um determinado valor é uma String.
veri = type(input("Informe algo: "))
if isinstance(veri, str):
    print("É uma string")
else:
    print("Não é uma string")




































































