import matplotlib.pyplot as plt

arquivo = open("pib.csv", 'r', encoding='UTF-8')
dados_crus = arquivo.read()
linhas = dados_crus.splitlines()
dados_crus_anos = linhas[0]
lista_anos = dados_crus_anos.split(",")
lista_anos.pop(0)

dados_crus_paises = linhas[1:]
lista_paises = []

for pais in dados_crus_paises:
    pais = pais.split(',')
    lista_paises.append(pais)

def busca(pais):
    for paises in lista_paises:
        for dados in paises:
            if pais in dados:
                paises.pop(0)
                plt.plot(lista_anos, paises, '^-')
                plt.ylabel("PIB (U$ Trilhões)")
                plt.xlabel("Anos")
                plt.suptitle(f'PIB - {pais} no período de 2013 a 2020')
                plt.show()
       

pais = input("Digite o Nome do País: ")
busca(pais)
