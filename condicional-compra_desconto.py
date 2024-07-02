#1 passo - entrada
import os
os.system('cls')

desc = str(input("Digite o nome do produto: "))
qtd = float(input("Digite a quantidade do produto: "))
preco_uni = float(input("Digite o preço unitario: "))
desc = 0


#2 passo - processamento
total = (qtd * preco_uni)
if qtd <= 5:
    desc = (preco_uni * 2)/100
elif qtd > 5 and qtd <= 10:
    desc = (preco_uni * 3)/100
elif qtd > 10:
    desc = (preco_uni * 5)/100

#3 passo - saída
print("O total a pagar é: ",total)
print("O total com desconto é: ",(total-desc))