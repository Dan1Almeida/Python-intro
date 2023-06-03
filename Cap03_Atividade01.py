import random

#Diferença entre int e round ... INT retira a parte decimal ... ROUND redonda

numero_secreto = int(93.954152158454)
print(numero_secreto)

numero_secreto = round(93.954152158454)
print(numero_secreto)

numero_secreto = int(random.random()* 100)
print(numero_secreto)

numero_secreto = random.randrange(0,101)
print(numero_secreto)