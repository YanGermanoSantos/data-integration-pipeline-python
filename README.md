# 📊 Pipeline de Integração de Dados (JSON + CSV)

Este projeto tem como objetivo construir um pipeline de dados simples utilizando Python, realizando a ingestão, transformação e consolidação de dados provenientes de diferentes fontes (JSON e CSV).

---

## 🚀 Objetivo

Unificar dados de duas empresas distintas em um único dataset estruturado, padronizando colunas e garantindo consistência para análises futuras.

---

## 🧱 Arquitetura do Pipeline

O projeto segue o padrão clássico de engenharia de dados:

* **Extract** → Leitura de arquivos JSON e CSV
* **Transform** → Padronização e tratamento dos dados
* **Load** → Escrita dos dados consolidados em arquivo final

---

## 📁 Estrutura do Projeto

```
.
├── data_raw/
│   ├── dados_empresaA.json
│   └── dados_empresaB.csv
│
├── data_processed/
│   └── dados_combinados.csv
│
├── notebooks/
│   └── exploracao.ipynb
│
├── scripts/
│   ├── processamento_dados.py
│   └── fusao_mercado_fev.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Tecnologias Utilizadas

* Python 3.x
* Biblioteca padrão:

  * `json`
  * `csv`

---

## 🔄 Etapas do Pipeline

### 📥 Extract

* Leitura de arquivos:

  * JSON (Empresa A)
  * CSV (Empresa B)
* Conversão para estrutura de dados em memória (listas de dicionários)

---

### 🔧 Transform

* Padronização de colunas
* Renomeação de campos para consistência entre datasets
* Validação de volume de dados
* Junção dos dados em uma única estrutura

Exemplo de mapeamento:

```python
key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}
```

---

### 📤 Load

* Escrita do dataset final em:

```
data_processed/dados_combinados.csv
```

---

## 🧠 Design do Código

O projeto utiliza uma abordagem orientada a objetos através da classe `Dados`, responsável por:

* Leitura de arquivos (`leitura_dados`)
* Padronização de colunas (`rename_columns`)
* Junção de datasets (`join`)
* Conversão para formato tabular
* Persistência dos dados (`salvando_dados`)

---

## ▶️ Como Executar o Projeto

### 1. Clone o repositório

```
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

---

### 2. Crie e ative o ambiente virtual

```
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

---

### 3. Instale as dependências

```
pip install -r requirements.txt
```

---

### 4. Execute o pipeline

```
python scripts/fusao_mercado_fev.py
```

---

## ✅ Saída Esperada

* Arquivo final consolidado:

```
data_processed/dados_combinados.csv
```
