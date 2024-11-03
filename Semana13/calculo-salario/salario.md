
# Cálculo de Salário Final de um Vendedor com Comissão

Este algoritmo foi desenvolvido para automatizar o cálculo do salário final de vendedores de uma revendedora de carros, com base em um sistema de comissão.

## Descrição do Problema
O cálculo considera os seguintes pontos:
1. **Salário Fixo**: cada vendedor recebe um valor fixo mensal.
2. **Comissão Fixa por Carro**: o vendedor recebe uma quantia adicional fixa para cada carro vendido.
3. **Percentual sobre o Total de Vendas**: o vendedor ganha 5% sobre o valor total de suas vendas.

## Regras de Negócio
Com base nas regras descritas, o cálculo verifica os seguintes casos:
1. **Salário Final Padrão**: se o número de carros vendidos for maior que zero, o vendedor recebe o salário fixo, a comissão por carro e 5% sobre o total das vendas.
2. **Salário Apenas Fixo**: se o número de carros vendidos for zero, o vendedor recebe apenas o salário fixo (sem comissão e sem percentual sobre vendas).
3. **Incentivo Adicional**: se o vendedor vender mais de 10 carros, ele recebe um bônus de 10% sobre o total das vendas.

## Tabela Verdade para Validação das Condições de Pagamento

| Número de Carros Vendidos | Total das Vendas | Salário Fixo | Comissão por Carro | Percentual sobre Vendas | Bônus de 10% | Salário Final |
|---------------------------|------------------|--------------|---------------------|-------------------------|--------------|---------------|
| 0                         | -                | Sim          | Não                | Não                     | Não          | Salário Fixo  |
| 1 a 10                    | >=0              | Sim          | Sim                | Sim (5%)                | Não          | Salário Fixo + Comissão + 5% sobre vendas |
| >10                       | >=0              | Sim          | Sim                | Sim (5%)                | Sim (10%)    | Salário Fixo + Comissão + 5% sobre vendas + 10% de bônus |

## Implementação do Algoritmo em Python

```python
def calcular_salario_final(salario_fixo, comissao_por_carro, total_vendas, carros_vendidos):
    # Salário base fixo
    salario_final = salario_fixo
    
    # Caso 1: Se o número de carros vendidos for maior que zero
    if carros_vendidos > 0:
        # Adiciona comissão fixa por carro
        salario_final += comissao_por_carro * carros_vendidos
        
        # Adiciona 5% sobre o total de vendas
        salario_final += 0.05 * total_vendas
        
        # Caso 3: Incentivo adicional para mais de 10 carros vendidos
        if carros_vendidos > 10:
            salario_final += 0.10 * total_vendas
            
    # Caso 2: Se o número de carros vendidos for zero, apenas o salário fixo é mantido.
    return salario_final

# Exemplo de uso
salario_fixo = 2000 
comissao_por_carro = 300
total_vendas = 50000
carros_vendidos = 12
# No código enviado, é possível que o usuário escreva esses valores. Esse é apenas um exemplo

salario_final = calcular_salario_final(salario_fixo, comissao_por_carro, total_vendas, carros_vendidos)
print(f"Salário Final do Vendedor: R$ {salario_final:.2f}")
```

## Explicação do Código
1. **Salário Fixo**: O valor fixo mensal é adicionado ao salário final.
2. **Comissão por Carro**: Se o número de carros vendidos for maior que zero, a comissão por carro vendido é calculada.
3. **Percentual sobre Vendas**: 5% sobre o total das vendas é adicionado ao salário.
4. **Incentivo Adicional**: Se o vendedor vender mais de 10 carros, ele recebe um bônus adicional de 10% sobre o total de vendas.

## Testes e Validação
A função `calcular_salario_final` pode ser chamada com diferentes valores para verificar se os casos da tabela verdade são atendidos.