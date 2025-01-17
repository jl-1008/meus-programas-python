
# Declarar os valores de faturamento por estado
faturamento_sp = 67836.43
faturamento_rj = 36678.66
faturamento_mg = 29229.88
faturamento_es = 27165.48
faturamento_outros = 19849.53

# Calcular o faturamento total
faturamento_total = (faturamento_sp + faturamento_rj + faturamento_mg + faturamento_es + faturamento_outros)

# Calcular a porcentagem de cada estado
percentual_sp = (faturamento_sp / faturamento_total) * 100
percentual_rj = (faturamento_rj / faturamento_total) * 100
percentual_mg = (faturamento_mg / faturamento_total) * 100
percentual_es = (faturamento_es / faturamento_total) * 100
percentual_outros = (faturamento_outros / faturamento_total) * 100

# Mostrar os resultados
print(f"Percentual de SP: {percentual_sp:.2f}%")
print(f"Percentual de RJ: {percentual_rj:.2f}%")
print(f"Percentual de MG: {percentual_mg:.2f}%")
print(f"Percentual de ES: {percentual_es:.2f}%")
print(f"Percentual de Outros: {percentual_outros:.2f}%")
