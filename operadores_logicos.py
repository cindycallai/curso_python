""" São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica. Quando um operador de 
comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores 
lógicos"""

# strings ou listas vazias são false

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

saldo = 1000
saque = 200
limite = 100
conta_especial = True

# Operador de comparação "and" = os dois precisam ser verdadeiros
saldo >= saque and saque <= limite

# Operador de comparação "or" = um dos dois precisa ser verdadeiro
saldo >= saque or saque <= limite

# Operador de comparação "not" = negação
not saldo >= saque or saque <= limite
not 1000 > 500

#Sem parênteses
exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)
# Com parênteses
exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

# comparação de contas
conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque
exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)