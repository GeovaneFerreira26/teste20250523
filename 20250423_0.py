while True:
    print("INICIANDO O PROGRAMA CALCULADORA")
    iniciar = input("Digite SIM - Continuar ou NÃO - SAIR: ").lower()
    if iniciar == "sim":
        
        def saudacao(nomes):
            for nome in nomes:
                print(f"Bem Vindo, {nome}")
                print()
        saudacao([input("Informe seu Nome: ")])
        
        while True:

            print("|QUAL CÁLCULO DESEJA EXECUTAR |")
            print("|DIGITE 1 - SOMAR             |")
            print("|DIGITE 2 - SUBTRAIR          |")
            print("|DIGITE 3 - MULTIPLICAR       |")
            print("|DIGITE 4 - DIVIDIR           |")
            print("|DIGITE 0 - SAIR              |")
            print()
            
            opcao = input("Opção escolhida: ")
            match(opcao):
                case "1":
                    def somar (num1, num2):
                        return num1 + num2
                    n1 = int(input("Informe o primeiro Valor: "))
                    n2 = int(input("Informe o segundo Valor: "))
                    resultado = somar(n1, n2) 
                    print(f"A Soma dos valores é {resultado}")
                    print()
                    
                case "2":
                    def subtracao (num1, num2):
                        return num1 - num2
                    n1 = int(input("Informe o primeiro Valor: "))
                    n2 = int(input("Informe o segundo Valor: "))
                    resultado = subtracao(n1, n2)
                    print(f"A Subtração dos valores é {resultado}")
                    print()
                    
                case "3":
                    def multiplicar (num1, num2):
                        return num1 * num2
                    n1 = int(input("Informe o primeiro Valor: "))
                    n2 = int(input("Informe o segundo Valor: "))
                    resultado = multiplicar(n1, n2)
                    print(f"A Multiplicação dos valores é {resultado}")
                    print()
                    
                case "4":
                    def dividir (num1, num2):
                        return num1 / num2
                    n1 = int(input("Informe o primeiro Valor: "))
                    n2 = int(input("Informe o segundo Valor: "))
                    resultado = dividir(n1, n2)
                    print(f"A Divisão dos valores é {resultado}")
                    print()
                    
                case "0":
                    break
    
    elif iniciar == "não":
        break            
                
                    
