from datetime import date

# Solicitar o salário ao usuário
salario = float(input("Digite o salário: "))

# Solicitar o percentual da PLR ao usuário
percentual_plr = float(input("Digite o percentual da PLR (em %): ")) / 100  # Converter para decimal

# Solicitar o ano e a data de início
ano = int(input("Digite o ano de início: "))
mes = int(input("Digite o mês de início (1-12): "))
dia = int(input("Digite o dia de início (1-31): "))
data_inicio = date(ano, mes, dia)

# Data de final do ano
data_fim = date(ano, 12, 31)

# Verificar se o ano é bissexto
total_dias_ano = 366 if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)) else 365

# Total de dias trabalhados
dias_trabalhados = (data_fim - data_inicio).days + 1  # +1 para incluir o dia de início

# Proporção de dias trabalhados
proporcao = dias_trabalhados / total_dias_ano

# Cálculo da PLR proporcional
plr_total = salario * percentual_plr
plr_proporcional = plr_total * proporcao

# Exibir os resultados
print(f"Total de dias trabalhados: {dias_trabalhados}")
print(f"Proporção de dias trabalhados: {proporcao:.2%}")
print(f"PLR proporcional: R$ {plr_proporcional:.2f}")