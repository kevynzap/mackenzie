# Laboratório CI/CD com GitHub Actions
## Nomes:
- Kevyn Zarpellon   RA: 10749524
- Matheus Eman      RA: 10749523

Projeto prático desenvolvido durante os estudos de **DevOps e DataOps**, com o objetivo de aplicar conceitos de Engenharia de Dados, testes automatizados e CI utilizando Python, Pytest e GitHub Actions.

Construir um pipeline simples de processamento de dados de vendas, desde a leitura de um arquivo CSV até a geração de uma tabela consolidada, utilizando boas práticas de desenvolvimento e automação.

O projeto também demonstra a aplicação de testes automatizados e integração contínua (CI), permitindo que o código seja validado automaticamente a cada alteração enviada ao GitHub.

**Repositório:** https://github.com/kevynzap/mackenzie

## Estrutura 
```bash
github/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── data/
│   └── vendas.csv
│
├── output/
│   └── vendas_processadas.csv
│
├── src/
│   ├── __init__.py
│   └── pipeline.py
│
├── tests/
│   ├── test_pipeline.py
│   ├── test_qtd.py
│   └── vendas_teste.csv
│
├── README.md
└── requirements.txt
```
## Fluxo do Processo
```bash
text
Arquivo CSV
    ↓
Leitura com Pandas
    ↓
Cálculo do valor total
    ↓
Agregação por produto
    ↓
Arquivo processado
    ↓
Testes automatizados com Pytest
    ↓
GitHub Actions (CI)
```