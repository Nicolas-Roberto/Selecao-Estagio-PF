import pandas as pd                         # importa a biblioteca pandas

df = pd.read_csv('Lista.csv', sep = ';')    # lê o arquivo csv e separa em função do ;

df = df.sort_values(by=['nome'])            # Ordena os valores pelo nome

print(df)                                   # Retorna uma lista com os registros ordenados pelo nome mais o índice, que é a posição da linha no arquivo csv



