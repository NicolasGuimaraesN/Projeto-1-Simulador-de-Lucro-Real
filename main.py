import pandas as pd

# 1. Simulação de Dados (Como se viessem de um banco SQL ou CSV)
data = {
    'data': ['2026-04-01', '2026-04-02', '2026-04-03', '2026-04-04', '2026-04-05'],
    'ganho_bruto': [250.00, 310.50, 180.00, 450.00, 380.00],
    'km_rodado': [120, 150, 80, 210, 170],
    'horas_online': [6, 8, 5, 10, 9],
    'consumo_medio_km_l': [35, 35, 35, 35, 35], # Ex: Consumo de uma moto
    'preco_combustivel': [5.80, 5.80, 5.80, 5.80, 5.80]
}

df = pd.DataFrame(data)

# 2. Cálculos de Ciência de Dados
# Custo de Combustível por dia
df['custo_combustivel'] = (df['km_rodado'] / df['consumo_medio_km_l']) * df['preco_combustivel']

# Estimativa de Manutenção/Depreciação (R$ 0,15 por km rodado)
df['depreciacao_manutencao'] = df['km_rodado'] * 0.15

# Lucro Líquido
df['lucro_liquido'] = df['ganho_bruto'] - df['custo_combustivel'] - df['depreciacao_manutencao']

# Ganho por Hora Líquido
df['lucro_por_hora'] = df['lucro_liquido'] / df['horas_online']

# 3. Exibição dos Resultados
print("--- Resumo de Performance ---")
print(df[['data', 'ganho_bruto', 'lucro_liquido', 'lucro_por_hora']].round(2))

print(f"\nLucro Total no Período: R$ {df['lucro_liquido'].sum():.2f}")
print(f"Média de Ganho Líquido por Hora: R$ {df['lucro_por_hora'].mean():.2f}")
