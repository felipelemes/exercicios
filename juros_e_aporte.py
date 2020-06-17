import matplotlib.pyplot as plt

montante_inicial = int(input("Informe o aporte inicial (R$): "))
rendimento_periodo = float(input("Informe o percentual de rendimento por período: "))
valor_aporte = int(input("Informe o valor de aporte por período (R$): "))
quantidade_de_períodos = int(input("Informe a quantidade de períodos: "))
periodos = []
montantes = []
print(f'Montante inicial: R${montante_inicial}')
print(f'Rendimento por período: {rendimento_periodo}%')
print(f'Valor de aporte por período: R${valor_aporte}')
print(f'Quantidade de períodos: {quantidade_de_períodos}')

montante = montante_inicial

for i in range (1,quantidade_de_períodos +1):
  montante_final_do_periodo = (montante * (1 + (rendimento_periodo/100)) + valor_aporte)
  print(f'Após {i} período(s), o montante total será de R${montante_final_do_periodo:.02f}.')
  periodos.append(i)
  montantes.append(montante_final_do_periodo)
  montante = montante_final_do_periodo

def desenha_grafico():
  plt.plot(periodos, montantes, '^-')
  plt.ylabel("Valor Acumulado (R$)")
  plt.xlabel("Período")
  plt.suptitle('Evolução do Valor Acumulado ao longo do tempo')
  plt.show()

desenha_grafico()