import numpy as np
from scipy import stats

jogadores = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]
np.mean(jogadores) # np = Numpy e mean = media
np.median(jogadores) # np = numpy e median = mediana
# [quartis para retorno 0%, 25%, 5%, 75%, 100% ]
quartis = np.quantile(jogadores,[0, 0.25, 0.5, 0.75, 1]) 
np.std(jogadores, ddof = 1) # STD= Standart Desviation, Desvio Padrão
stats.describe (jogadores)