maisb = ""
preçob = float("inf")
soma = 0

for x in range(5):
    med = input("Nome do remédio: ")
    preco = float(input("Preço do remédio:"))

    if preco < preçob:
        precob = preco
        medicamentobarato = med
    soma += x
media = soma / 5
print(medicamentobarato, precob, media)