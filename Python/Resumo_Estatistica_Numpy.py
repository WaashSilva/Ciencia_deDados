# O conjunto de dados contém os seguintes números:
# nunca: 5 uma vez: 8 duas vezes: 4, 3 vezes: 3
# Calcule e imprima a variância
import numpy as np
a = np.array ([5,
                10,10,
                2,2,2,2,
                3,3,3])
mean = np.sum (a)/a.size
v = np.sum((a-mean)**2)/a.size
print (mean)
print (v)
# meas == 1.25
# v == 0.9875

# Calcular desvio padrão
import numpy as np 
list = [8,8,8,8,8] 
print(np.std(list))

# Calcular a variancia
import numpy as np 
list = [2, 4, 4, 4, 5, 5, 7, 9] 
print(np.var(list))

# Calcular a média
import numpy as np 
list = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190] 
print(np.average(list))

# O código fornecido inclui uma lista de alturas para vários
# jogadores de basquete.
# Você precisa calcular e produzir quantos jogadores 
# estão na faixa de um desvio padrão da média
players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
import numpy as np
mean = np.mean(players)
standard_deviation = np.std(players)
variance = np.var(players)
result = 0
for i in players:
    if i >= mean-standard_deviation and i <= mean+standard_deviation:
        result += 1
print(result)

# SHAPE retorna tuplas, refere o numero de linhas e colunas na matriz
# SIZE retorna numero total de elementos na matriz
# NDIM retorna o numero de dimensoes da matriz

#Podemos adicionar, remover e ordenar um array usando as funções
# (), () e (). np.append np.delete np.sort Por exemplo:
import numpy as np
x = np.array ([2, 1, 3])
# Adiciona um elemento
x = np.append (x, 4)
# Deleta um indice
x = np.delete(x, 0)
# Ordena o Array
x = np.sort(x)

# EXEMPLO
import numpy as np
x = np.arange(2, 8, 2)
x = np.append(x, x.size)
x = np.sort(x)
print(x[1])
# print == 3

# SHAPE se refere ao número de linhas e colunas na matriz.
# EXEMPLO
import numpy as np
x = np.arange(1,7)
print (x)
# print [1,2,3,4,5,6]
# NumPy nos permite alterar a forma de nossos arrays usando
# a função reshape().
z = x.reshape(3,2)
print (z)
# Print [[1 2]
#         [3 4]
#          [5 6]]

# Reshape também pode fazer o oposto: pegue um array
# bidimensional e faça um array unidimensional a partir dele:
import numpy as np
x = np.array([[1,2],[3,4],[5,6]])
z = x.reshape(6)
print (x)
print (z)
# X== [[1 2]
#       [3 4]
#        [5 6]]
# z == [1 2 3 4 5 6]
# O mesmo resultado pode ser obtido usando a função flatten ().

# EXEMPLO 2
import numpy as np
x = np.arange(1, 8, 3)
z = x.reshape(3, 1)
print(z[1][0])
# Print == 4

# As matrizes NumPy podem ser indexadas e divididas 
# da mesma maneira que as listas do Python. Por exemplo:
import numpy as np
x = np.arange (1,10)
print (x[0:2]) # [1,2]
print (x[5:]) # [6,7,8,9]
print (x[:2]) # [1,2]
print (x[-3:]) #  [7,8,9]
print (x[-1]) # [9]
# Índices negativos contam a partir do final da matriz,
# portanto, [-3:] resultará nos últimos 3 elementos.

# Selecionar elementos menores que algum numero
import numpy as np
x = np.arange (1, 10)
print (x[x<4]) # [1,2,3]
# As condições podem ser combinadas usando (and) ou (or) operadores.
# Por exemplo, vamos pegar os números pares que são maiores que 5:
print (x[x>5]) or ([x%2==0]) # [array([False,  True, False,  True, False,  True, False,  True, False])]
print (x[x>5]) and ([x%2==0]) #[1, 2, 3] , [6, 7, 8, 9]

#EXEMPLO 2
import numpy as np
x = np.array([11, 42, 8, 5, 18])
z = x[x>15]
print(z.size)

# É fácil realizar operações matemáticas básicas com arrays.
# Por exemplo, para encontrar a soma de todos os elementos, usamos a função sum ():
import numpy as np
x = np.arange (1,10) # [1 2 3 4 5 6 7 8 9]
print (x.sum()) # 45
# Da mesma forma, min () e max () podem ser usados ​​para obter os elementos menores e maiores.
# Multiplicar todos os elementos por 2
y = x*2
print (y) # [ 2  4  6  8 10 12 14 16 18]

# calcular a media,mediana,variancia e desvio padrão dos valores do array
import numpy as np
x = np.array([14, 18, 19, 24, 26, 33, 42, 55, 67])
print (np.mean(x)) # media == 33.111111111111114
print (np.median(x)) # mediana == 26.0
print (np.var(x)) # variancia == 292.5432098765432
print (np.std(x)) # desvio padrão == 17.10389458212787

# Você recebe uma matriz que representa os preços das casas.
# Calcule e imprima a porcentagem de casas que estão dentro de um desvio padrão da média .
import numpy as np
data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])
m = np.mean(data)
s = np.std(data)
low = m-s
high = m+s
print(
    len(data[(low < data) & (data < high)])
     / len(data) *100
)
