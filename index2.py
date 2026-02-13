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
    
#9)  Faça um algoritmo que verifica se um determinado valor é do tipo decimal.
num = input("Informe o um valor número: ")
if "." or "," in num:
    print("O número é decimal.")
else:   
    print("O número é inteiro.")
    
# 10) Faça um algoritmo que leia três números e imprima na tela o maior deles.
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))
if num1 > num2 and num1 > num3:
    print("O maior número é:", num1)
elif num2 > num1 and num2 > num3:
    print("O maior número é:", num2)
else:
    print("O maior número é:", num3)

# 12) Faça um algoritmo que leia três números e imprima-os em ordem crescente.
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

ordem = sorted([num1, num2, num3])
print("Números em ordem crescente:", ordem)

# 13) Faça um algoritmo que leia um caractere e informe se o mesmo é uma vogal ou não.
letra = str(input("Digite a letra: "))
if letra in ['a', 'e', 'i', 'o', 'u']:
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")
# 14) Os endereços IP versão 4 são divididos em cinco classes: A, B, C, D e E. 
# Os endereços no intervalo de 0 à 127 são classe A, de 128 a 191 são classe B, de 192 a 223 são classe C, de 224 à 239 são classe D e a partir de 240 são classe E. Faça um algoritmo que leia o primeiro octeto, no formato decimal de um endereço IP, e informe a sua classe.


ip = int(input("Informe a classe do IP v4: "))
if ip in [0, 127]:
    print("Classe A")
elif ip in range(128, 191):
    print("Classe B")
elif ip in range(192, 223):
    print("Classe C")
elif ip in range(224, 239):
    print("Classe D")
else:
    print("Classe E")


# 15) 
#Faça um algoritmo que receba um número inteiro, que represente um determinado mês do ano, e mostre o nome do mês correspondente. 
#Por exemplo, se for informado o número 2, o algoritmo deverá exibir: fevereiro. 
#O algoritmo também deve validar se a entrada está correta.
num_mes = int(input("Digite o número do mês (1-12): "))

if num_mes == 1:
    print("Janeiro") 
elif num_mes == 2:
    print("Fevereiro")
elif num_mes == 3:
    print("Março")
elif num_mes == 4:
    print("Abril")
elif num_mes == 5: 
    print("Maio")
elif num_mes == 6:
    print("Junho")
elif num_mes == 7:
    print("Julho")
elif num_mes == 8:  
    print("Agosto")
elif num_mes == 9:
    print("Setembro")
elif num_mes == 10:
    print("Outubro")
elif num_mes == 11:
    print("Novembro")
elif num_mes == 12:
    print("Dezembro")
else:
    print("Número inválido. Por favor, digite um número entre 1 e 12.")

# 16)  Faça um algoritmo que valide uma data. A mesma deve ser formada por dia, mês e ano. Por exemplo, se o usuário digitar a data 10/8 a mesma será inválida. 
# Porém, caso a data seja 01/10/2018, a mesma deve ser considerada válida.

data = input("Digite a data (dd/mm/aaaa): ")

partes = data.split("/")

if len(partes) != 3:
    print("Data inválida.")
else:
    dia = partes[0]
    mes = partes[1]
    ano = partes[2]

    if dia.isdigit() and mes.isdigit() and ano.isdigit():
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)

        if 1 <= mes <= 12 and 1 <= dia <= 31 and ano > 0:
            print("Data válida.")
        else:
            print("Data inválida.")
    else:
        print("Data inválida.")







































