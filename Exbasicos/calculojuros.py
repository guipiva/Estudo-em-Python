deposito = int(input("Digite o valor do deposito: "))
juros = int(input("Digite o valor do juros: "))
juross = deposito * (juros/100)
total = deposito + juross

print(f"O valor total é:{total} e o redimento foi de:{juross}")

