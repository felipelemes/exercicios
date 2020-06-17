arquivo = open("pib.csv", 'r', encoding='UTF-8')
dados_crus = arquivo.read()
linhas = dados_crus.splitlines()
dados_crus_anos = linhas[0]
lista_anos = dados_crus_anos.split(",")
dados_crus_paises = linhas[1:]
lista_paises = []

for pais in dados_crus_paises:
    pais = pais.split(',')
    lista_paises.append(pais)

def lista_variacao():
    for pais in lista_paises:
        variacao = (float(pais[-1]) - float(pais[1]))
        print(f'{pais[0]}       Variação de {variacao:.2f}% no PIB entre 2013 e 2020')

lista_variacao()