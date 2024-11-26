from datetime import date

# Solicitar o salário e a data de início ao usuário
salario = float(input("Digite o salário: "))
percentual_plr = 0.97  # Percentual fixo da PLR

# Solicitar a data de início
ano = 2024
mes = int(input("Digite o mês de início (1-12): "))
dia = int(input("Digite o dia de início (1-31): "))
data_inicio = date(ano, mes, dia)

# Data de final do ano
data_fim = date(2024, 12, 31)

# Total de dias no ano e dias trabalhados
total_dias_ano = 366  # 2024 é um ano bissexto
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