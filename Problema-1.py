
# 1 Criação de um dicionário
My_dict = { 'João'  :21,
            'Maria' : 30,
            'Matheus' : 15,
            'Ana' : 15,
            }

# 2 Criação de uma lista vazia para os valores
Valores = []

# 3 adição dos valores do dicionário na lista Valores sem repetições de valores
for Chave , Valor in My_dict.items():   # For que percorre o dicionário pegando as chaves e os valores
    if type(Chave) == str:              # Verifíca se a Chave é uma string
        if Valor not in Valores:        # Verifíca se o valor da chave não esta na lista com os valores
            Valores.append(Valor)           # Adiciona o valor na lista de valores



print(Valores)


