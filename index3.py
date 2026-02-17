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
    



































































