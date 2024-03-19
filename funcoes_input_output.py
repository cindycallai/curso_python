"""A função builtin input é utilizada quando queremos ler dados da entrada padrão (teclado). Ela recebe um argumento do tipo string, 
que é exibido para o usuário na saída padrão (tela). A função lê a entrada, converte para string e retorna o valor.
"""

# input
nome = input("Informe o seu nome: ")
sobrenome = input("Informe o seu sobrenome: ")
idade = input("Informe a sua idade: ")

# output
print(nome, sobrenome, idade)
print(nome, sobrenome, idade, end="...\n") #quebra de linha
print(nome, sobrenome, idade, sep="#", end="...\n") #quebra de linha
print(nome, sobrenome, idade, sep="#") # separador