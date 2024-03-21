curso = "pYtHoN"

# Converte tudo para maiúsculo
print(curso.upper())
# Converte tudo para minúsculo
print(curso.lower())
# Converte primeira letra para maiúsuclo
print(curso.title())

texto = "   Cindy   "
# Remove os espaços em branco da esquerda e da direita
print(texto.strip() + ".")
# Remove os espaços em branco da esquerda
print(texto.lstrip() + ".")
# Remove os espaços em branco da direita
print(texto.rstrip() + ".")

texto1 = "Guilherme"
# Centralização de string: Centralizado e com # no inicio e fim e com 10 caracteres
print(texto1.center(15, "#"))
print(texto1.center(15))
# Junção, nesse caso com o ponto
print(".".join(texto1))
print("-".join(texto1))
