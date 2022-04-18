# Qual a chance de um conjunto de objetos de uma caixa ser...
# Media = 8 desvio padrão (dp) = 2 < 6
pnorm (6,8,2) * 100

# Qual a chance de eu tirar um objeto que tenha mais de 6 kg ?
# Opção 1:

pnorm (6, 8, 2, lower.tail=F) * 100
# Opção 2:
(1 - pnorm (6, 8, 2)) * 100

# Qual a chance de tirar um objeto que tenha menos de 
  # 6 kg ou mais de 10kg ?
(pnorm (6,8,2) + pnorm (10,8,2, lower.tail=F)) * 100

# Qual a chance de tirar um objeto que tenha > 10kg e < 8KG
(pnorm (10, 8, 2) - pnorm (8, 8, 2)) * 100

#gerar diagrama de normalidade com a função qqnorm
# como gerar dados aleatorios normalmente distribuidos
x = rnorm(100)

# Grafico de normalidade
qqnorm(x)
qqline(x)
shapiro.test(x)
