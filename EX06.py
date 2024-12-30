import math

n1 = int(input("Digite um valor: "))
dobro = n1 * 2
triplo = n1 * 3
raiz = pow(n1,(1/2))
#raiz = math.sqrt(n1) OUTRA FORMA DE FAZER
#raiz = n1 ** (1/2) OUTRA FORMA DE FAZER
print("O dobro do valor é: {}\n"
      "O triplo do valor é: {}\n"
      "Sua raiz quadrada é: {:.2f}".format(dobro,triplo,raiz))