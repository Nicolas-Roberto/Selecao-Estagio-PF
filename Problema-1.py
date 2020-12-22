
# 1 Criação de um dicionário
My_dict = { 'João'  :21,
            'Maria' : 30,
            'Carlos' : 15,
            'Ana' : 15,
            }

# 2 Criação de uma lista vazia para os valores
Valores = []

#3 Criação de uma variável exit recebendo False
exit = False

# 4 Repete a Função até exit ser diferente de False
while exit == False:

    Chave = str(input('Digite uma chave ou Digite 0 para sair: '))   # Pega uma chave digitada pelo usuário, converte em string e coloca na variável Chave
    
    if Chave == '0':                      # Caso Chave seja igual a 0 em string encerra o while
        break

    if Chave in My_dict:                 # Verifíca se a Chave existe dentro do dicionário

        Valor = My_dict.get(Chave)       # Cria uma variável valor com o valor da chave digitada dentro do dicionário

        if Valor not in Valores:         # Se o Valor não estiver na lista Valores
            Valores.append(Valor)        # A lista Valores adiciona o Valor
            print('Valor adicionado.')
        else:
            print('Valor ja foi adicionado.')   

    else:                               # Se não devolve o texto Chave não encontrada  
        print('Chave não encontrada.')    


print(Valores)                          # Retorna um print da lista Valores


