# Os dois componentes principais dos pandas são o Series e o DataFrame
# Uma série é essencialmente uma coluna e um DataFrame é uma tabela
# multidimensional composta por uma coleção de séries.

# Antes de trabalhar com dados reais, vamos primeiro criar um DataFrame
# manualmente para explorar suas funções.
# A maneira mais fácil de criar um DataFrame é usando um dictionary :
import pandas as pd
data = {
        'ages': [14, 18, 24, 42],
        'heights': [165 ,180 ,176, 184]
}
df = pd.DataFrame(data)

# Quantas colunas tem o seguinte DataFrame ?
import pandas as pd
x = { 'a': [1, 2],
     'b': [3, 4],
     'c': [5, 6] }
df = pd.DataFrame(x)
# Resposta 3

# O DataFrame cria automaticamente um index numérico para cada linha.
# Podemos especificar um índice personalizado, ao criar o DataFrame:
import pandas as pd
df = pd.DataFrame (data, index=['james', 'bob', 'amy', 'Dave'])
print (df.loc['bob']) # ages: 18, heights: 180, Name: bob, dtype: int64

# Podemos selecionar uma única coluna especificando seu nome entre colchetes:
print (df['ages'])  # james    14
                    # bob      18
                    # amy      24
                    # Dave     42
                    # Name: ages, dtype: int64
                    
# O resultado é um objeto Series . Se quisermos selecionar várias colunas,
# podemos especificar uma lista de nomes de colunas:
print (df[['ages','heights']])        # ages  heights
                                      # james    14      165
                                      # bob      18      180
                                      # amy      24      176
                                      # Dave     42      184


# Pandas usa a função iloc para selecionar dados com base em seu índice numérico.
# Funciona da mesma maneira que listas de indexação em Python. Por exemplo:
print (df.iloc[2])                      #ages        24
                                        #heights    176
                                        #Name: amy, dtype: int64
print (df.iloc[:3])                           #ages  heights
                                      #james    14      165
                                      #bob      18      180
                                      #amy      24      176
print (df.iloc[1:3])                         #ages  heights
                                      #bob    18      180
                                      #amy    24      176
                                      
# Retorna as 5 primeiras linhas                                      
print (df.head())

# Retorna as 5 ultimas linhas                                      
print (df.tail())

# A função info() é usada para obter informações essenciais sobre seu conjunto
# de dados, como número de linhas, colunas, tipos de dados, etc:
df.info()

# Agora que nosso conjunto de dados está limpo e configurado, estamos prontos
# para analisar algumas estatísticas!
# A função describe () retorna as estatísticas de resumo para todas as colunas
# numéricas:
df.describe()

# A função groupby () é usada para agrupar nosso conjunto de dados pela coluna
# fornecida. Também podemos calcular o número total de casos no ano inteiro:
# Exemplo
df.groupby('mounth')['cases'].sum ()

# TRABALHO
# Você está trabalhando com o conjunto de dados COVID para a Califórnia, que 
# inclui o número de casos e mortes para cada dia de 2020.
# Encontre o dia em que a razão mortes/casos foi maior.
# Para fazer isso, você precisa primeiro calcular a proporção de óbitos/casos 
# e adicioná-la como uma coluna ao DataFrame com o nome 'ratio', depois 
# encontrar a linha que corresponde ao maior valor.
import pandas as pd
df = pd.read_csv("/usercode/files/ca-covid.csv")
df.drop('state', axis=1, inplace=True)
df.set_index('date', inplace=True)
df['ratio']= df['deaths']/ df['cases']
maxratio =df.loc[df['ratio']==df['ratio'].max()]
print(maxratio)











































































