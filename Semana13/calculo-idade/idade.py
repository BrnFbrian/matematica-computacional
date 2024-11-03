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
