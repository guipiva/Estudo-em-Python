larg = float(input("Digite a largura da parede: "))
alt = float(input("Digite a altura da parede: "))
calculo = larg * alt
tinta = calculo/2
print(f"Sua parede tem a dimensao de {larg}x{alt} e sua area total é {calculo}"
      f" Para pintar essa parede voce vai precisar de {tinta:.2f}L de tinta")

