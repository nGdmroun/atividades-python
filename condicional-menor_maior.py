valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
if valor1 > valor2:
    print("Maior",valor1)
    print("Menor",valor2)
elif valor1 < valor2:
    print("Menor",valor1)
    print("Maior",valor2)
else:
    print("Valores iguais")