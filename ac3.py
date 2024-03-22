"""
Autor: Marcelle Lohane Gonçalves Ganimo
Programação Estruturada 
2024.01
AC3 exercícios 1, 2 e 3

"""
# Exercício 1

def determina_tipo_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        match a, b, c:
            case a, b, c if  a == b == c:
                return "Equilátero"  
            case a, b, c if a != b == c:
                return "Isósceles"
            case a, b, c if b != c == a:
                return "Isósceles"
            case a, b, c if c != b == a:
                return "Isósceles"
            case a, b, c if a != b != c: 
                return "Escaleno"
    else:
        return "Não é um triângulo"

print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo



#  Exercício 2 
def dia_semana(dia):
    # Recebe um número inteiro e retorna uma string indicando o dia da semana
    if dia == 1:
        return "domingo"
    elif dia == 2:
        return "segunda-feira"
    elif dia == 3:
        return "terça-feira"
    elif dia == 4:
        return "quarta-feira"
    elif dia == 5:
        return "quinta-feira"
    elif dia == 6:
        return "sexta-feira"
    elif dia == 7:
        return "sábado"
    else: 
        return ""
    
print(dia_semana(2)) # segunda-feira
print(dia_semana(6)) # sexta-feira
print(dia_semana(7)) # sábado
print(dia_semana(9)) # string vazia

#Exercício 3 

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return ""

def calculadora():
    x = float(input("Informe um número: "))
    y = float(input("Informe outro número: "))
    operador = input("Informe a operação: ")

    if operador == "soma":
        resultado = soma(x, y)
    elif operador == "subtração":
        resultado = subtracao(x, y)
    elif operador == "multiplicação":
        resultado = multiplicacao(x, y)
    elif operador == "divisão":
        resultado = divisao(x, y)
    else:
        resultado = "Operação inválida!"

    print("Resultado:", resultado)

calculadora()
