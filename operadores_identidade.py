# São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória.

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 1000, 500

# comparando se ambos estão na mesma região de memória
print(curso is nome_curso)

# comparando se não estão na mesma região de memória
print(curso is not nome_curso)

# comparando se ocupa a mesma região de memória
print(saldo is limite)

