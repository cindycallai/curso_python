# inteiro -> float
preco = 10
print(preco)
preco = float(preco)
print(preco)

# float -> inteiro
preco = 10.30
print(preco)
preco = int(preco)
print(preco)

# Conversão por divisão
preco = 10
print(preco / 2) #float
print(preco // 2) #inteiro

# numérico -> string
preco = 10.50
idade = 28
print(str(preco))
print(str(idade))
# Concatenar string com variáveis
texto = f"idade {idade} preco {preco}"
print(texto)

# string -> número
preco = "10.50"
idade = "28"
print(float(preco))
print(float(idade))

"""# erro na conversão
preco = "python"
print(float(preco)) """

# mostrando o tipo da variável
valor = 10
valor_str = str(valor)
print(type(valor))
print(type(str(valor)))