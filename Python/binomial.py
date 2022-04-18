from scipy.stats import binom
# Jogar uma moeda 5 vezes, qual a probabilidade de dar cara 3 vezes ?
prob = binom.pmf(3, 5, 0.5)
# Passar por 4 sinais de 4 tempos, qual a probabilidade de pegar
    # sinal verde, 0, 1, 2, 3, 4 vezes seguidas ?
binom.pmf(0, 4, 0.25)
binom.pmf(1, 4, 0.25)
binom.pmf(2, 4, 0.25)
binom.pmf(3, 4, 0.25)
binom.pmf(4, 4, 0.25)

# Com sinais de 2 tempos:
binom.pmf(0, 4, 5)
binom.pmf(1, 4, 5)
binom.pmf(2, 4, 5)
binom.pmf(3, 4, 5)
binom.pmf(4, 4, 5)

#probabilidade acumulativa
binom.cdf(4, 4, 0.25)

#Concurso com 12 questoes, qual a probabilidade de acertar 7 questoes
#considerando que cada questão possue 4 alquernativas ?
binom.pmf(7, 12, 0.25) * 100
#Acertar todas as questões
binom.pmf(12, 12, 0.25) * 100
