from scipy.stats import norm

# Conjunto de objetos de uma cesta, a media é de 8 e o desvio padrão é 2
    # Qual a probabilidade de tirar um objeto que o peso é menor que 6 kg

# (qual o valor a ser retirado, media, desvio padrão (dp))
norm.cdf(6, 8, 2) * 100

# qual a probabilidade de retirar um objeto < 6 kg
# Opção 1:
norm.sf(6, 8, 2) * 100

# Opção 2:
(1 - norm.cdf (6, 8, 2)) * 100

# Qual a prbabilidade de tirar um objeto que o peso é menor que 6 ou maior
    # que 8 kg ?
(norm.cdf (6, 8, 2) + norm.sf (10, 8, 2)) * 100

# Qual a probabilidade de tirar um objeto que o peso é menor que 10 e maior
    # que 8 kg ?
(norm.cdf (10, 8, 2) - norm.cdf (8, 8, 2)) * 100
