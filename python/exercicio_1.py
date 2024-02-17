#Escreva uma classe Fração que defina a soma, a subtração, a multiplicação e a divisão de frações sobrecarregando-se os operadores padrões para essas operações. 
#Escreva um membro de função para fatores de redução e sobrecarga dos operadores de E/S , para entrar e sair com frações.


import math

class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        mdc = math.gcd(self.numerador, self.denominador)
        self.numerador //= mdc
        self.denominador //= mdc

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, outra):
        novo_numerador = self.numerador * outra.denominador + outra.numerador * self.denominador
        novo_denominador = self.denominador * outra.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __sub__(self, outra):
        novo_numerador = self.numerador * outra.denominador - outra.numerador * self.denominador
        novo_denominador = self.denominador * outra.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __mul__(self, outra):
        novo_numerador = self.numerador * outra.numerador
        novo_denominador = self.denominador * outra.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __truediv__(self, outra):
        novo_numerador = self.numerador * outra.denominador
        novo_denominador = self.denominador * outra.numerador
        return Fracao(novo_numerador, novo_denominador)

# Teste
f1 = Fracao(3, 4)
f2 = Fracao(1, 2)

print("Fracao 1:", f1)
print("Fracao 2:", f2)

soma = f1 + f2
print("Soma:", soma)

subtracao = f1 - f2
print("Subtracao:", subtracao)

multiplicacao = f1 * f2
print("Multiplicacao:", multiplicacao)

divisao = f1 / f2
print("Divisao:", divisao)
