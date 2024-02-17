"""
Escreva um programa simples de reserva de bilhetes de linha aérea. O programa exibe um menu com as seguintes opções: 
reserva de bilhete, cancelamento de bilhete, verificação se um bilhete está reservado para uma pessoa em particular 
e exibição dos passageiros. A informação é mantida em ordem alfabética numa lista ligada de nomes. Em uma versão mais 
simples do programa, assuma que os bilhetes estão reservados para somente um voo. Numa versão mais completa, não coloque 
limite no número de voos. Crie uma lista ligada de voos com cada nó incluindo um ponteiro para uma lista ligada de passageiros.
"""
class Passageiro:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.primeiro = None

    def adicionar_passageiro(self, nome):
        novo_passageiro = Passageiro(nome)
        if not self.primeiro:
            self.primeiro = novo_passageiro
        else:
            atual = self.primeiro
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_passageiro

    def listar_passageiros(self):
        if not self.primeiro:
            print("Não há passageiros na lista.")
        else:
            atual = self.primeiro
            while atual:
                print(atual.nome)
                atual = atual.proximo

class Voo:
    def __init__(self, numero):
        self.numero = numero
        self.passageiros = ListaLigada()
        self.proximo = None

class ListaVoos:
    def __init__(self):
        self.primeiro = None

    def adicionar_voo(self, numero):
        novo_voo = Voo(numero)
        if not self.primeiro:
            self.primeiro = novo_voo
        else:
            atual = self.primeiro
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_voo

    def encontrar_voo(self, numero):
        atual = self.primeiro
        while atual:
            if atual.numero == numero:
                return atual
            atual = atual.proximo
        return None

def menu():
    print("1. Reserva de bilhete")
    print("2. Cancelamento de bilhete")
    print("3. Verificação de reserva por nome")
    print("4. Exibição de passageiros")
    print("5. Sair")

def main():
    lista_voos = ListaVoos()
    lista_voos.adicionar_voo("Voo 1")

    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            numero_voo = input("Digite o número do voo: ")
            voo = lista_voos.encontrar_voo(numero_voo)
            if voo:
                nome_passageiro = input("Digite o nome do passageiro: ")
                voo.passageiros.adicionar_passageiro(nome_passageiro)
                print("Bilhete reservado com sucesso.")
            else:
                print("Voo não encontrado.")
        elif escolha == "2":
            # Implementação do cancelamento de bilhete
            pass
        elif escolha == "3":
            # Implementação da verificação de reserva por nome
            pass
        elif escolha == "4":
            numero_voo = input("Digite o número do voo: ")
            voo = lista_voos.encontrar_voo(numero_voo)
            if voo:
                print("Passageiros do voo", numero_voo)
                voo.passageiros.listar_passageiros()
            else:
                print("Voo não encontrado.")
        elif escolha == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()

