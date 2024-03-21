# Executar até o número ser igual a 10
while True:
   if numero == 10:
        break
   
print(numero, end=" ")

# Com o FOR também é possível
for numero in range(100):
    if numero == 10:
        break
print(numero, end=" ")

# Com continue: pula uma condição.
while True:
   numero = int(input("Informe um número: "))
   if numero == 10:
       break
   if numero % 2 == 0:
       continue
   print(numero, end=" ")