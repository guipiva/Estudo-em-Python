sexo = 0
media = 0
maior = 0
menor = 0
contador = 0
peso = 0
nome_chave = 0
for c in range (0,4):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if idade> maior:
            maior = peso
        if idade < menor:
            menor = peso
    sexo = input("Digite o sexo: ")
    if (sexo == "masculino"):
        sexo = 1
    else:
        sexo = 2

    if sexo == 2 and idade == menor:
        contador += 1

    if sexo == 1 and idade == maior:
        nome == nome_chave

    media = idade / 4

print(media)
print(nome_chave)
print(contador)
