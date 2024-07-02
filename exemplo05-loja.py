print("Calculando a Parcelas")
print("--------------------------")

#1 Passo - Entrada
input("Digite o nome do produto: \n")
valor_produto = float (input("Digite o valor da  Compra: \n"))
quant_compra = int (input("Digite a quantidade de produtos: \n"))

#2 passo - Processamento de dados 
valor_total = valor_produto * quant_compra
num_parcelas = int (input("Coloque o numero de parcelas que deseja fazer: \n"))

#3 passo - saida 
valor_parcela = valor_total / num_parcelas
print(" O Valor Total da sua compra foi de: ", valor_total, "reais \n\n o Valor unitario do produto custa: ", valor_produto, "reais\n\n foi parcelado em: ", num_parcelas, "vezes \n\n Cada parcela sera no valor de: ", valor_parcela, "reais")
