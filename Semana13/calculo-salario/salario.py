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

# Solicita os dados do usuário
salario_fixo = float(input("Digite o salário fixo do vendedor: R$ "))
comissao_por_carro = float(input("Digite o valor da comissão por carro vendido: R$ "))
total_vendas = float(input("Digite o valor total das vendas: R$ "))
carros_vendidos = int(input("Digite o número de carros vendidos: "))

# Calcula o salário final
salario_final = calcular_salario_final(salario_fixo, comissao_por_carro, total_vendas, carros_vendidos)

# Exibe o salário final do vendedor
print(f"\nSalário Final do Vendedor: R$ {salario_final:.2f}")
