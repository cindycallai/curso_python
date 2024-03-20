# É através da indentação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

def sacar(self, valor: float): # início do bloco do método

    if self.saldo >= valor: # início do bloco do if

        self.saldo -= valor

    # fim do bloco if

# fim do bloco do método

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("Retire seu dinheiro")

    print("Obrigado por ser nosso cliente!")

sacar(1000)

def depositar(valor):
saldo = 500 #erro de identação
saldo+=valor