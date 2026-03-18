from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# ========================
# EXTRACT
# ========================
print("\n[EXTRACT] Iniciando leitura dos dados...")

dados_empresaA = Dados.leitura_dados(path_json, 'json')
print(f"[EXTRACT][Empresa A - JSON] Colunas: {dados_empresaA.nome_colunas}")
print(f"[EXTRACT][Empresa A - JSON] Linhas: {dados_empresaA.qtd_linhas}")

dados_empresaB = Dados.leitura_dados(path_csv, 'csv')
print(f"[EXTRACT][Empresa B - CSV] Colunas: {dados_empresaB.nome_colunas}")
print(f"[EXTRACT][Empresa B - CSV] Linhas: {dados_empresaB.qtd_linhas}")

# ========================
# TRANSFORM
# ========================
print("\n[TRANSFORM] Iniciando transformação dos dados...")

key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

dados_empresaB.rename_columns(key_mapping)
print(f"\n[TRANSFORM][Empresa B] Colunas renomeadas: {dados_empresaB.nome_colunas}")

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f"[TRANSFORM][JOIN] Colunas finais: {dados_fusao.nome_colunas}")
print(f"[TRANSFORM][JOIN] Total de linhas: {dados_fusao.qtd_linhas}")

# ========================
# LOAD
# ========================
print("\n [LOAD] Salvando dados processados...")

path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)

print(f"[LOAD] Arquivo salvo com sucesso em: {path_dados_combinados}")
print("[PIPELINE FINALIZADO]")