renda_mensal_total = int(input("Informe sua renda mensal total (R$): "))
gastos_totais_com_moradia = int(input("Informe seus gastos totais com moradia(R$): "))
gastos_totais_com_educacao = int(input("Informe seus gastos totais com educação(R$): "))
gastos_totais_com_transporte = int(input("Informe seus gastos totais com transporte(R$): "))
porcentagem_moradia = ((gastos_totais_com_moradia)/(renda_mensal_total)) * 100
porcentagem_educacao = ((gastos_totais_com_educacao)/(renda_mensal_total)) * 100
porcentagem_transporte = ((gastos_totais_com_transporte)/(renda_mensal_total)) * 100
gasto_total_recomendado_moradia = 0.3 * renda_mensal_total
gasto_total_recomendado_educacao = 0.2 * renda_mensal_total
gasto_total_recomendado_transporte = 0.15 * renda_mensal_total

print('\n'f'Renda Mensal: R${renda_mensal_total}')
print(f'Gastos totais com moradia : R${gastos_totais_com_moradia}')
print(f'Gastos totais com educação: R${gastos_totais_com_educacao}')
print(f'Gastos totais com transporte: R${gastos_totais_com_transporte}')

print('\n' "Diagnóstico:")
if(porcentagem_moradia > 30):
  print('\n' f'Seus gastos totais com moradia comprometem {porcentagem_moradia}% de sua renda total. O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {gasto_total_recomendado_moradia}.')
else:
  print(f'Seus gastos totais com moradia comprometem {porcentagem_moradia}2% de sua renda total. O máximo recomendado é de 30%. Seus gastos estão dentro da margem recomendada.')
if(porcentagem_educacao > 20):
  print(f'Seus gastos totais com educação comprometem {porcentagem_educacao}% de sua renda total. O máximo recomendado é de 20%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {gasto_total_recomendado_educacao}.')
else:
  print(f'Seus gastos totais com educação comprometem {porcentagem_educacao}% de sua renda total. O máximo recomendado é de 20%. Seus gastos estão dentro da margem recomendada.')
if(porcentagem_transporte > 30):
  print(f'Seus gastos totais com transporte comprometem {porcentagem_transporte}% de sua renda total. O máximo recomendado é de 15%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {gasto_total_recomendado_transporte}.')
else:
  print(f'Seus gastos totais com transporte comprometem {porcentagem_transporte}% de sua renda total. O máximo recomendado é de 15%. Seus gastos estão dentro da margem recomendada.')