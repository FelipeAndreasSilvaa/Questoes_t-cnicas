import json
import os

def calcular_faturamento(filepath):
    if not os.path.isfile(filepath):
        print(f"Arquivo não encontrado: {filepath}")
        return

    with open(filepath, 'r') as file:
        data = json.load(file)

    faturamento_diario = data['faturamento']
    
    # Filtrar valores válidos (não zero)
    valores_validos = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]
    
    if not valores_validos:
        print("Não há dias com faturamento.")
        return

    menor_valor = min(valores_validos)
    maior_valor = max(valores_validos)
    media_mensal = sum(valores_validos) / len(valores_validos)

    # Contar dias com faturamento acima da média
    dias_acima_media = sum(1 for dia in faturamento_diario if dia['valor'] > media_mensal)

    # Resultados
    print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
    print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

# Chamar a função com o caminho para o arquivo JSON
calcular_faturamento('faturamento.json')  # Verifique se o nome do arquivo está correto
