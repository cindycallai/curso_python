"""O comando FOR é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de vezes que nosso bloco 
   de código deve ser executado, ou quando queremos percorrer um objeto iterável.
"""
# Exibe as vogais do texto digitado
texto = input("Informe um texto: ")

VOGAIS = "AEIOU"

for letra in texto:
	if letra.upper() in VOGAIS:
		print(letra, end="")
		
print()  # adiciona uma quebra de linha

# Funciona da mesma forma com o FOR/ELSE
for letra in texto:
	if letra.upper() in VOGAIS:
	   print(letra, end="")
else:   
	print()  # adiciona uma quebra de linha

# FOR com a função range
for numero in range(0,11):
	print(numero, end=" ")

# Exibindo a tabuada do 5
for numero in range(0, 51, 5): # começa do 0, máximo 51, de 5 em 5.
	print(numero, end=" ")