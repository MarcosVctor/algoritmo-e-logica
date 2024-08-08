a = int(input("Informe um numero inteiro: "))
b = int(input("Informe outro número inteiro: "))
soma = 0

if (a < b):
    for termo in range (a, b):
        soma += termo
    print(soma)
else:
    print("Erro, tente novamente")  
