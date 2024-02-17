class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        else:
            return None

    def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        else:
            return None

    def esta_vazia(self):
        return len(self.itens) == 0

def inverter_palavra(palavra):
    pilha = Pilha()
    for letra in palavra:
        pilha.empilhar(letra)

    palavra_invertida = ""
    while not pilha.esta_vazia():
        palavra_invertida += pilha.desempilhar()

    return palavra_invertida

def verificar_palindromo(palavra):
    return palavra == inverter_palavra(palavra)

def menu():
    print("\nMENU:")
    print("1. Verificar nova cadeia de caracteres")
    print("2. Sair")

def main():
    while True:
        cadeia = input("Digite uma cadeia de caracteres (ou 'sair' para encerrar): ")
        if cadeia.lower() == "sair":
            print("Saindo...")
            break

        print("Cadeia digitada:", cadeia)
        inverso = inverter_palavra(cadeia)
        print("Inverso:", inverso)

        if verificar_palindromo(cadeia):
            print("A cadeia é um palíndromo.")
        else:
            print("A cadeia não é um palíndromo.")

        while True:
            menu()
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                break
            elif escolha == "2":
                print("Saindo...")
                return
            else:
                print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
