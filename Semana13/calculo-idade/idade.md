
# Cálculo Demográfico - Antropologia

Este programa calcula dois valores baseados nas idades de dois homens e duas mulheres:

1. A **soma** da idade do homem mais velho com a mulher mais nova.
2. O **produto** da idade do homem mais novo com a mulher mais velha.

## Descrição do Problema
Um estudo antropológico busca relacionar certas variáveis demográficas com uma regra específica:
- Para o cálculo da idade total, precisamos da soma entre a idade do homem mais velho e a da mulher mais nova.
- Para o cálculo do produto, precisamos multiplicar a idade do homem mais novo pela idade da mulher mais velha.

## Regras de Negócio
1. O algoritmo deve identificar o homem mais velho e o homem mais novo, assim como a mulher mais velha e a mais nova, a partir das idades fornecidas.
2. A idade do homem mais velho deve ser somada com a idade da mulher mais nova.
3. A idade do homem mais novo deve ser multiplicada pela idade da mulher mais velha.

## Código em Python

```python
def solicitar_idade(descricao):
    while True:
        try:
            idade = int(input(f"Digite a idade do {descricao}: "))
            if idade <= 0:
                print("Erro: A idade deve ser um número inteiro positivo. Tente novamente.")
            else:
                return idade
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número inteiro positivo.")

def calcular_soma_produto(homem1, homem2, mulher1, mulher2):
    # Identificar o homem mais velho e o mais novo
    homem_mais_velho = max(homem1, homem2)
    homem_mais_novo = min(homem1, homem2)
    
    # Identificar a mulher mais velha e a mais nova
    mulher_mais_velha = max(mulher1, mulher2)
    mulher_mais_nova = min(mulher1, mulher2)
    
    # Calcular a soma e o produto de acordo com as regras
    soma = homem_mais_velho + mulher_mais_nova
    produto = homem_mais_novo * mulher_mais_velha
    
    return soma, produto

# Solicitação de idades de maneira interativa e amigável
print("Bem-vindo ao programa de cálculo demográfico! Vamos solicitar as idades para fazer os cálculos.")
homem1 = solicitar_idade("primeiro homem")
homem2 = solicitar_idade("segundo homem")
mulher1 = solicitar_idade("primeira mulher")
mulher2 = solicitar_idade("segunda mulher")

# Cálculo e exibição dos resultados
soma, produto = calcular_soma_produto(homem1, homem2, mulher1, mulher2)
print("\nResultados:")
print(f"A soma da idade do homem mais velho com a mulher mais nova é: {soma}")
print(f"O produto da idade do homem mais novo com a mulher mais velha é: {produto}")
```

## Instruções
1. Insira as idades de dois homens e duas mulheres, conforme solicitado.
2. O programa verificará automaticamente se as idades são válidas (inteiros positivos).
3. O resultado apresentará a soma e o produto das idades conforme as regras descritas.

**Observação:** Este código deve ser executado em um ambiente que suporte entradas de usuário, como um terminal ou um editor que aceite a função `input()`.

## Resultado Esperado
- **Exemplo:** Se as idades fornecidas são 30 e 25 (homens) e 20 e 22 (mulheres), o programa deve identificar:
  - Homem mais velho: 30
  - Homem mais novo: 25
  - Mulher mais velha: 22
  - Mulher mais nova: 20

- Resultado:
  - Soma do homem mais velho com a mulher mais nova: 30 + 20 = 50
  - Produto do homem mais novo com a mulher mais velha: 25 * 22 = 550
