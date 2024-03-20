# A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

MAIOR_IDADE = 18 #constante
IDADE_ESPECIAL = 12

idade = int(input("Informe a sua idade: "))

# if simples
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
if idade < MAIOR_IDADE:
    print("Menor de idade, não pode tirar a CNH")

# if com dois desvios
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
else:
    print("Menor de idade, não pode tirar a CNH")

# if com mais de dois desvios   
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas")
else:
    print("Menor de idade, não pode tirar a CNH")

