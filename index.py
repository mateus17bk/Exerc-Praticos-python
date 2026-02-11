#1) Escreva um programa em Python que exiba a mensagem "Olá mundo" na tela.
print("Olá mundo")

#2) Faça um programa que solicite ao usuário o seu nome e exiba na tela a mensagem: O seu nome é [nome digitado]


nome = input("Informe do seu nome: ")
print("O seu nome é " + nome)

#3) Desenvolva um programa que peça ao usuário seu nome e sua idade e exiba uma frase informando esses dados.


nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
print("O seu nome é " + nome + " e sua idade é " + idade)



#4) Crie um programa que solicite um número ao usuário e mostre na tela o número informado.  
num = input("Digite um número: ")
print("O númerero é: " + num)

#5) Faça um programa que leia três números inteiros e exiba a soma total deles.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
print("A soma dos números total é: ", int(num1+num2+num3))


#6) Elabore um programa que receba quatro notas de um aluno e calcule a média aritmética.
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))
print("A média da nota é: ", float(nota1+nota2+nota3+nota4)/4)

#7) Crie um programa que receba uma medida em metros e converta para centímetros.
metros = float(input("Informe a medidade em metros: "))
print("A medida convertida em centímetros: ", float(metros*100))


#8) Desenvolva um programa que receba um número e mostre o valor do seu quadrado e do seu cubo.

num1 = float(input("Digite um número: "))
print("o valor do cubo é: ", num1**2 , "E o valor do quadrado é: ", num1**3)


#9) Faça um programa que receba dois números e exiba o resto da divisão entre eles, mostrando o resultado em formato decimal e inteiro.

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
print("Valor decimal", float((num1%num2)), "Valor inteiro", int((num1%num2)))


#10) Crie um programa que receba a altura e a largura de um retângulo e calcule sua área.
alt = float(input("Informe a altura: "))
larg = float(input("Informe a largura: "))
print("A área do retangulo é: ", float((alt*larg)))
      
#11) Elabore um programa que receba uma quantidade de dias, horas, minutos e segundos e converta todo o tempo informado para segundos.

qtd_dias = int(inpu("Quantidade em dias: "))
qtd_hora = int(input("Quantidade horas: "))
qtd_minu = int(input("Quantidade minutos: "))
qtd_segund = int(input("Quantidade segundos: "))
print("O valor convertido para segundos é: ", init(qtd_dias*86400) + init(qtd_hora*3600) + init(qtd_minu*60) + init(qtd_segund))

#12) Faça um programa que receba um valor e calcule o desconto de 10% sobre ele, exibindo o valor do desconto.
valor = float(input("Digite um valor: "))
print("O valor do desconto é:", valor * 0.10, "R$ reais")


