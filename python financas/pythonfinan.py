# total dias por ano
anos = 365

#total semanas por ano
semanas = 52

nome = input("Digite o seu Nome:")
# total horas de trabalho por dia 
total_horas_trabalho_dias = int(input('Quantas horas tu trabalhas por dia?: '))
total_dias_de_trabalho_por_semana = int(input('Quantos dias tu trabalha por semana?: '))
Salaraio_anual = float(input('Qual o valor do seu salario anualmente?: '))

#calculando total horas de trabalho por ano
total_horas_semanalmenteA = total_horas_trabalho_dias * total_dias_de_trabalho_por_semana
total_horas_trabalho_por_ano = semanas * total_horas_semanalmenteA


# calculando o salario por horas
Salario_por_horas = Salaraio_anual / total_horas_trabalho_por_ano

# calculando o Salario diario
Salario_diario = Salario_por_horas * total_horas_trabalho_dias

# calculando Salario semanal
Salario_semanal = Salaraio_anual / semanas

#calculando Salario Mensal
Salario_mensal = Salaraio_anual / 12

# Calculando o Salario anual
Salario_bruto_anual = Salario_mensal * 12

print('\n=========== Informação do funcionario ===============')
print('Nome: '+nome)
print('Total Horas de trabalho por dia: ' + str(total_horas_trabalho_dias))
print('Total Dias de trabalho por semana: ' + str(total_dias_de_trabalho_por_semana))
print('\n=========== Informação de salario ===============\n')
print('Salario por horas: R$ {:,.2f} '.format(Salario_por_horas))
print('Salario por dia: R$ {:,.2f} '.format(Salario_diario))
print('Salario por semana: R$ {:,.2f} '.format(Salario_semanal))
print('Salario por mes: R$ {:,.2f} '.format(Salario_mensal))
print('Salario por ano: R$ {:,.2f} '.format(Salaraio_anual))
