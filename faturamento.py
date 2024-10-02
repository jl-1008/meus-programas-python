
import json

# Passo 1: Carregar os dados de faturamento de um arquivo JSON
with open('faturamento.json', 'r') as file:
    dados = json.load(file)

# Extraímos o vetor de faturamento diário
faturamento = dados['faturamento_diario']

# Passo 2: Encontrar o menor e o maior valor de faturamento (ignorando dias com 0)
faturamento_validos = [dia for dia in faturamento if dia > 0]  # Ignorar dias sem faturamento (0)

menor_faturamento = min(faturamento_validos)  # Menor valor
maior_faturamento = max(faturamento_validos)  # Maior valor

# Passo 3: Calcular a média mensal de faturamento (somente dias com faturamento)
media_faturamento = sum(faturamento_validos) / len(faturamento_validos)

# Passo 4: Contar quantos dias tiveram faturamento acima da média
dias_acima_media = 0
for dia in faturamento_validos:
    if dia > media_faturamento:
        dias_acima_media += 1

# Passo 5: Mostrar os resultados
print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
print(f"Média de faturamento: R$ {media_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
