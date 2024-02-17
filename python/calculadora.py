def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

def main():
    while True:
        print("\nSelecione a operacao:")
        print("1. Adicao")
        print("2. Subtracao")
        print("3. Multiplicacao")
        print("4. Divisao")
        print("5. Sair")

        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print("Resultado:", soma(num1, num2))
            elif escolha == '2':
                print("Resultado:", subtracao(num1, num2))
            elif escolha == '3':
                print("Resultado:", multiplicacao(num1, num2))
            elif escolha == '4':
                print("Resultado:", divisao(num1, num2))
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção invalida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
