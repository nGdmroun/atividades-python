import os
os.system('cls')

#passo 1 - entrada
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
operacao = int(input("\nDigite a operação:\n1-> Soma\n2-> Subtração\n3-> Divisão\n4-> Multiplicação\n"))
resultado = 0

#passo 2 - processamento 
if operacao == 1:
    resultado = (num1 + num2)
elif operacao == 2:
    resultado = (num1 - num2)
elif operacao == 3:
    resultado = (num1/num2)
elif operacao == 4:
    resultado = (num1*num2)

#passo 3 - saída
print("O resultado da operação é: ",resultado)