print("Seja Bem-Vindo ao Boletim Eletrônico!")

#Entrada
nome = input ("Digite seu nome: ")
p1 = float(input("Digite sua Primeira Nota:"))
p2= float(input("Digite sua Segunda Nota:"))
p3= float(input("Digite sua Terceira Nota:"))
p4= float(input("Digite sua QuartaNota:"))

#Processamento
media= (p1+p2+p3+p4)/4

#saida
print("ALuno:" ,nome,"Sua média é:",media)