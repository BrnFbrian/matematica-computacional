# Calcular a razão das partes formadas pela bissetriz interna e externa de um triângulo.
def calcular_bissetriz_interna(b, c):
    return b / c


# Calcular a razão das partes formadas pela bissetriz externa no lado oposto.
def calcular_bissetriz_externa(a, b, c):
    return (a + b) / c


# Entrada de dados dos lados do triângulo
try:
    a = float(input("Digite o valor do lado a: "))
    b = float(input("Digite o valor do lado b: "))
    c = float(input("Digite o valor do lado c: "))

    # Validação para garantir que os valores formam um triângulo
    if a + b > c and a + c > b and b + c > a:
        # Cálculos
        razao_interna = calcular_bissetriz_interna(b, c)
        razao_externa = calcular_bissetriz_externa(a, b, c)

        # Exibição dos resultados
        print(
            f"A razão das partes formadas pela bissetriz interna é: {razao_interna:.2f}"
        )
        print(
            f"A razão das partes formadas pela bissetriz externa é: {razao_externa:.2f}"
        )
    else:
        print("Os valores inseridos não formam um triângulo válido.")
except ValueError:
    print("Por favor, insira apenas valores numéricos.")
