#Calculadora do Diogo Rangel

def menu():
    print("="*35)
    print("\033[1;32m[1] Soma (+)")
    print("[2] Subtração (-)")
    print("[3] Multiplicação (*)")
    print("[4] Divisão (/)")
    print("[5] Sair")
    print("\033[1;36m" + "="*35 + "\033[m")

soma = lambda x, y: x + y
sub = lambda x, y: x - y
mult = lambda x,y: x * y

def divisao (x, y):
    if y == 0:
        return "ERROR"
    else:
        return x / y

while True:
    print("\033[1;36m" + "="*35)
    print("        🧮 CALCULADORA 🧮")
    print("="*35)
    try:
        menu()
        op = int(input("Escolha uma opção acima: "))
        if op == 5:
            print("Programa encerrado!")
            break
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
       
        if op == 1:
            print(f"{num1} + {num2} =", end=' ')
            print(soma(num1, num2))
        elif op == 2:
            print(f"{num1} - {num2} =", end=' ')
            print(sub(num1, num2))
        elif op == 3:
            print(f"{num1} * {num2} =", end=' ')
            print(mult(num1, num2))
        elif op == 4:
            print(f"{num1} / {num2} =", end=' ')
            print(divisao(num1, num2))
        else:
            print("Opção inválida!")

    except Exception:
        print("Ops! Esse não é um número válido. Tente novamente...")
