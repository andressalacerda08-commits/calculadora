def soma (valor1, valor2):
    soma = valor1 + valor2
    return soma
def subtair (valor1, valor2):
    subtrair = valor1 - valor2
    return subtrair
def multiplicar (valor1, valor2):
    multiplicar = valor1 * valor2
    return multiplicar
def divisao (valor1, valor2):
    divisão = valor1 / valor2
print("CALCULADORA")
print("DIGITE A SUA OPRAÇÃO!")
valor1 = float(input("Digite o valor1: "))
operacao = input("Digite operação desejada: ")
valor2 = float(input("Digite o valor2: "))
if operacao == "+": 
    resultado = soma(valor1, valor2)
elif operacao == "-":
    resultado = subtair(valor1, valor2)
elif operacao == "*":
    resultado = multiplicar(valor1, valor2)
elif operacao == "/":
    resultado = divisao(valor1, valor2)
else:
    print("ERRO/VALOR INVÁLIDO")
print(resultado)