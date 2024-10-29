
# Atividade 2: Teorema da Bissetriz Interna e Externa

Este documento explica passo a passo a lógica do algoritmo para calcular a razão das partes formadas pela bissetriz interna e externa em um triângulo. Além disso, aborda como o código lida com casos especiais, como divisão por zero e a verificação da validade do triângulo.

## Código Completo

O código Python permite que o usuário insira os valores dos lados do triângulo e, em seguida, calcula a razão das partes divididas pelas bissetrizes interna e externa. O código completo está abaixo:

```python
def calcular_bissetriz_interna(b, c):
    """
    Calcula a razão das partes formadas pela bissetriz interna no lado oposto.
    """
    return b / c if c != 0 else None  # Evita divisão por zero

def calcular_bissetriz_externa(a, b, c):
    """
    Calcula a razão das partes formadas pela bissetriz externa no lado oposto.
    """
    return (a + b) / c if c != 0 else None  # Evita divisão por zero

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
        if razao_interna is not None:
            print(f"A razão das partes formadas pela bissetriz interna é: {razao_interna:.2f}")
        else:
            print("Divisão por zero na bissetriz interna. Verifique os valores de entrada.")

        if razao_externa is not None:
            print(f"A razão das partes formadas pela bissetriz externa é: {razao_externa:.2f}")
        else:
            print("Divisão por zero na bissetriz externa. Verifique os valores de entrada.")
    else:
        print("Os valores inseridos não formam um triângulo válido.")
except ValueError:
    print("Por favor, insira apenas valores numéricos.")
```

## Explicação Passo a Passo

1. **Definição das Funções de Cálculo**
   - `calcular_bissetriz_interna(b, c)`: Esta função calcula a razão da bissetriz interna no lado oposto. A função retorna o valor da razão se o lado `c` for diferente de zero; caso contrário, retorna `None` para evitar uma divisão por zero.
   - `calcular_bissetriz_externa(a, b, c)`: Esta função calcula a razão da bissetriz externa. Semelhante à função anterior, ela retorna `None` caso o lado `c` seja zero.

2. **Entrada de Dados**
   - O código solicita que o usuário insira os valores dos lados do triângulo (`a`, `b` e `c`). Estes valores são convertidos para o tipo `float` para garantir que possam ser utilizados em operações matemáticas.

3. **Validação do Triângulo**
   - Para garantir que os valores fornecidos formem um triângulo válido, é aplicada a desigualdade triangular. Essa verificação confirma se a soma de quaisquer dois lados é sempre maior que o terceiro lado.

4. **Cálculos das Razões**
   - Se o triângulo é válido, o código chama as funções `calcular_bissetriz_interna` e `calcular_bissetriz_externa` para determinar as razões das divisões formadas pelas bissetrizes.

5. **Tratamento de Casos Especiais**
   - O código verifica se os resultados das funções de cálculo são `None`, o que indicaria uma tentativa de divisão por zero. Nesse caso, exibe uma mensagem de aviso específica para o usuário.

6. **Exibição dos Resultados**
   - Os valores calculados para as razões são exibidos com duas casas decimais. Caso ocorra uma divisão por zero, uma mensagem específica orienta o usuário a revisar os valores inseridos.

7. **Tratamento de Exceções**
   - Se o usuário insere um valor que não é numérico, ocorre uma exceção `ValueError`, e uma mensagem de erro é exibida, orientando a entrada de valores numéricos.

## Casos Especiais

1. **Divisão por Zero**
   - A divisão por zero é tratada diretamente nas funções `calcular_bissetriz_interna` e `calcular_bissetriz_externa`. Elas retornam `None` em caso de tentativa de divisão por zero, e o código principal lida com isso ao verificar se o resultado é `None`.

2. **Valores Inválidos para o Triângulo**
   - O código garante que apenas valores que formem um triângulo válido sejam processados, evitando cálculos incorretos.

3. **Entradas Não Numéricas**
   - Para evitar erros de tipo, o código possui um bloco `try-except` que captura entradas não numéricas e exibe uma mensagem de orientação ao usuário.

## Considerações Finais

Este código permite calcular as razões formadas pelas bissetrizes interna e externa de um triângulo, além de lidar com casos especiais para garantir sua robustez. Para verificar o funcionamento, execute o código em um ambiente Python e insira diferentes valores para testar as verificações implementadas.

