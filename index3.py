# 1) Faça um algoritmo que imprima os números no intervalo entre 1 e 100:
for x in range(1,101,1):
    print(x)

# 2) Evolua o algoritmo no qual imprimimos os números num intervalo pré-definido para um algoritmo que pergunte ao usuário qual o intervalo que o mesmo deseja que seja impresso:
num_inicio = int(input("Informe o inicio: "))
num_fim = int(input("Informe o fim: "))

while(num_inicio<=num_fim):
    print(num_inicio)
    num_inicio +=1
print("fim da operação")

#3) Faça um algoritmo que imprima os números no intervalo entre 1 e 10 em ordem inversa:
print (list(range(10,0,-1)))

#4) Faça um algoritmo que imprima os números pares entre 0 e 100:
x = 0
for x in range(100):
    x +=1
    print(x)

# 5) Faça um algoritmo que some a quantidade de números pares encontrados no intervalo entre 0 e 100:
x = 0
for x in range(100):
    x +=1
    if(x%2==0):
        print(x)

#6) Faça um algoritmo que imprima os números primos entre 0 e 100:

x = 0
for x in range(100):
    x +=1
    if(x%2==1):
        print(x)


#7) Faça um algoritmo que calcule os número primos num intervalo pré-determinado pelo usuário:
num_inicio = int(input("Informe o inicio: "))
num_fim = int(input("Informe o fim: "))
num_inicio = 0
while(num_inicio<=num_fim):
    num_inicio +=1
    if(num_inicio%2==1):
        print(num_inicio)

#8) Faça um algoritmo que imprima os valores no intervalo definido pelo usuário e permita que o mesmo possa definir 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela:
num_inicio = int(input("Informe o inicio: "))
num_fim = int(input("Informe o fim: "))
exec_1 = int(input("Retirar o primeiro número: "))
exec_2 = int(input("Retirar o segundo número: "))
exec_3 = int(input("Retirar o terceiro número:  "))
for exibir in range(num_inicio,num_fim):
    if exibir not in (exec_1,exec_2,exec_3):
        print(exibir,"\n")
    else:
        print()


































































