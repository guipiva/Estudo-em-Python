numero = int(input("Entre com o numero: "))
fatorial = 1
if numero < 0:
    print("O Fatorial nao existe!")
elif numero == 0:
    print("O Fatorial é 1!")
else:
    for i in range (1, numero+1):
        fatorial = fatorial*i
    print(f"O fatorial de {numero} é igual a {fatorial}")

