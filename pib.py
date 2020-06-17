import csv


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

def busca_ano(ano):
    indice = None
    if ano in lista_anos:
        indice = lista_anos.index(f'{ano}')
        return indice
    else:
        return indice

def busca_pais(pais,indice):
    for paises in lista_paises:
        for dados in paises:
            if pais in dados:
                pib = paises[indice]
                return True, pib

ano = input("Informe um ano entre 2013 e 2020: ")

if (busca_ano(ano) == None):
    print('Ano não encontrado!')
else:
    pais = input("Digite o nome do país: ")
    try:
        x, y = busca_pais(pais,busca_ano(ano))
        print(f'PIB de {pais} em {ano}: U${y} trilhões.')
    except:
        print("País não encontrado!")





#try:
    #print(f'PIB {pais} em {ano}: U${pib} trilhões')
#except:
    #print("Não foi possível localizar os dados solicitados. Verifique o nome do país e o ano solicitado.")




def variacao_pib():
    pass