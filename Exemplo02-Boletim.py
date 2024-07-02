print("Bem vindo ao Boletim Eletronio")

# 1 Passo - Entrada de Dados 
nome= input("Digite seu nome: ")

p1 = float (input("Digite sua Primeira Nota: "))
p2 = float (input("Digite sua Segunda Nota: "))
p3 = float (input("Digite sua Terceira Nota: "))
p4 = float (input("Digite sua Quarta Nota: "))

# 2 passo - Processamento
media = (p1+p2+p3+p4)/4

# 3 passo - Saida
print ("Aluno:", nome,", sua média foi:", media)
input ("Pressione <ENTER> para continuar")