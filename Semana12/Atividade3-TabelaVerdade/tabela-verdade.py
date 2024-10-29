import pandas as pd
import itertools

# Define possíveis valores verdade para as proposições
valores_verdade = [True, False]

# Gera todas as combinações de valores verdade para P, Q, R, M
cenarios = list(itertools.product(valores_verdade, repeat=4))

# Inicializa a tabela para armazenar cada linha de valores verdade e avaliações
tabela_verdade = []

for P, Q, R, M in cenarios:
    # Condições
    cond1 = not P or Q  # P -> Q
    cond2 = (P or Q) <= R  # (P v Q) -> R
    cond3 = (not P) <= (R == M)  # ~P -> (R <-> M)
    
    # Resultado: todas as condições devem ser verdadeiras
    resultado = cond1 and cond2 and cond3
    
    # Adiciona a linha à tabela
    tabela_verdade.append([P, Q, R, M, cond1, cond2, cond3, resultado])

# Converte para DataFrame
colunas = ["P (Ana vai)", "Q (Bruno vai)", "R (Festa animada)", "M (Bruno traz música)", 
           "Cond1 (P -> Q)", "Cond2 ((P v Q) -> R)", "Cond3 (~P -> (R <-> M))", "Resultado"]
df_tabela_verdade = pd.DataFrame(tabela_verdade, columns=colunas)

# Exibe a tabela
print(df_tabela_verdade)
