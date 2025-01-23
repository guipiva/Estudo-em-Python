def primo(numero):
    eprimo = False
    resto = 0

    for c in range (1, numero):
        if (numero%c)==0:
            resto += 1

    if resto == 1:
        eprimo = True

    return eprimo

n = int(input("Entre com um valor inteiro, positivo e maior que zero: "))

if primo(n):
    print(f"O numero {n} é primo")
else:
    print(f"O numero {n} não é primo")