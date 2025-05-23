# DEF - especifica do Python

#def somar(num1, num2, num3):
 #   return num1+ num2+ num3

#resultado = somar(2, 4, 5)
#print(f"A Soma dos valores é: {resultado}")

#def MaiorMenor(num1, num2):
    #if num1 < num2:
    #    return num2
    #elif num1 > num2:
   #     return num1
  #  else:
 #       return("OS dois são iguais")
    
#numero1 = int(input("Digite o Primeiro Número: "))
#numero2 = int(input("Digite o Segundo Número: "))
#resultado = MaiorMenor(numero1, numero2)
#print(f"O Maior Número é {resultado}")


def saudacao(listar_nomes):
    for nome in listar_nomes:
        print(f"Olá, {nome}")
        
saudacao(['Jamille', 'Geovane', 'Jéssica', 'Jennifer'])