import os
os.system('cls')

#Passo 1 - entrada
nivel = int(input("Digite o nível do professor: "))
qtd_aulas_semana = int(input("Digite a quantidade de horas por semana: "))
salario = 0

#Passo 2 - processamento 
if nivel == 1:
    salario = qtd_aulas_semana * 12
    print("O salario total do professor de Nível",nivel,",com",qtd_aulas_semana,"horas trabalhadas é de:",salario)
elif nivel == 2:
    salario = qtd_aulas_semana * 17
    print("O salario total do professor de Nível",nivel,",com",qtd_aulas_semana,"horas trabalhadas é de:",salario)
elif nivel ==3:
    salario = qtd_aulas_semana * 25
    print("O salario total do professor de Nível",nivel,",com",qtd_aulas_semana,"horas trabalhadas é de:",salario)
else:
    print("Nível Inexistente ")
    