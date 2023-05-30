def soma():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(num1+num2)
    
def div():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(num1/num2)
    
def sub():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(num1-num2)

def mult():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(num1*num2)

def expo():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(num1**num2)


operador = 1

while operador:
        print("Operadores da calculadora")
        print("1 - Somar")
        print("2 - Dividir")
        print("3 - Subtrair")
        print("4 - Multiplicar")
        print("5 - Exponenciação")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            soma()
        elif opcao == 2:
            div()
        elif opcao == 3:
            sub()
        elif opcao == 4:
            mult()
        elif opcao == 5:
            expo()
        else:
            print("Digito inválido")

  
        









        