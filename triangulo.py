# Função para verificar semelhança pelo critério LAL (Lado-Ângulo-Lado)
def verificar_semelhanca_LAL(triangulo1, triangulo2):
    lado1_1, angulo_1, lado1_2 = triangulo1
    lado2_1, angulo_2, lado2_2 = triangulo2

    # Verifica se os lados são proporcionais e o ângulo entre eles é congruente
    if (lado1_1 / lado2_1 == lado1_2 / lado2_2) and (angulo_1 == angulo_2):
        return True
    return False

# Função para verificar semelhança pelo critério AA (Ângulo-Ângulo)
def verificar_semelhanca_AA(triangulo1, triangulo2):
    angulo1_1, angulo1_2 = triangulo1
    angulo2_1, angulo2_2 = triangulo2

    # Verifica se dois ângulos são congruentes
    if (angulo1_1 == angulo2_1 and angulo1_2 == angulo2_2) or (angulo1_1 == angulo2_2 and angulo1_2 == angulo2_1):
        return True
    return False

# Função para verificar semelhança pelo critério LLL (Lado-Lado-Lado)
def verificar_semelhanca_LLL(triangulo1, triangulo2):
    lado1_1, lado1_2, lado1_3 = triangulo1
    lado2_1, lado2_2, lado2_3 = triangulo2

    # Verifica se todos os lados são proporcionais
    if (lado1_1 / lado2_1 == lado1_2 / lado2_2 == lado1_3 / lado2_3):
        return True
    return False

# Função para coletar as informações do triângulo
def obter_triangulo(criterio):
    if criterio == "LAL":
        lado1 = float(input("Digite o valor do primeiro lado do triângulo: "))
        angulo = float(input("Digite o valor do ângulo entre os lados: "))
        lado2 = float(input("Digite o valor do segundo lado do triângulo: "))
        return (lado1, angulo, lado2)

    elif criterio == "AA":
        angulo1 = float(input("Digite o valor do primeiro ângulo do triângulo: "))
        angulo2 = float(input("Digite o valor do segundo ângulo do triângulo: "))
        return (angulo1, angulo2)

    elif criterio == "LLL":
        lado1 = float(input("Digite o valor do primeiro lado do triângulo: "))
        lado2 = float(input("Digite o valor do segundo lado do triângulo: "))
        lado3 = float(input("Digite o valor do terceiro lado do triângulo: "))
        return (lado1, lado2, lado3)

# Função principal para verificar a semelhança
def verificar_semelhanca(triangulo1, triangulo2, criterio):
    if criterio == "LAL":
        return verificar_semelhanca_LAL(triangulo1, triangulo2)
    elif criterio == "AA":
        return verificar_semelhanca_AA(triangulo1, triangulo2)
    elif criterio == "LLL":
        return verificar_semelhanca_LLL(triangulo1, triangulo2)
    else:
        print("Critério inválido.")
        return False

# Programa principal
criterio = input("Escolha o critério de semelhança (LAL, AA, LLL): ").upper()

print("Digite os valores para o primeiro triângulo:")
triangulo1 = obter_triangulo(criterio)

print("Digite os valores para o segundo triângulo:")
triangulo2 = obter_triangulo(criterio)

resultado = verificar_semelhanca(triangulo1, triangulo2, criterio)

if resultado:
    print(f"Os triângulos são semelhantes pelo critério {criterio}.")
else:
    print(f"Os triângulos não são semelhantes pelo critério {criterio}.")
    