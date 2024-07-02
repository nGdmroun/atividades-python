print("CONVERSÃO DE MOEDA")

#1 PASSO - ENTRADA 
ValorDolar = float (input("Digite a quantidade de dolares que voce quer converter: \n"))
Cotacao = float (input("Digite a cotação atual do dolar: \n"))

#2 passo - processamento 

ValorReal =  ValorDolar * Cotacao

#3 passo - Saida 

print(f"Voce Esta Convertendo:  {ValorDolar:.2f} Dolares \n\n Após a Conversão, Recebera:  {ValorReal:.2f} reais")