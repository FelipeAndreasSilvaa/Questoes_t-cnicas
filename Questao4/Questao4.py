# Dados de faturamento por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Cálculo do faturamento total
total_faturamento = sum(faturamento.values())

# Cálculo do percentual de cada estado
percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento.items()}

# Exibição dos resultados
print("Percentual de representação do faturamento por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
