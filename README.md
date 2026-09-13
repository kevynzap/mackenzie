# Laboratório CI/CD com GitHub Actions
## Nomes:
- Kevyn Zarpellon   RA: 10749524
- Matheus Eman      RA: 10749523

Este repositório foi criado como um laboratório prático para estudo dos conceitos de DevOps, DataOps e CI/CD, utilizando GitHub Actions e uma aplicação simples em Python.

O objetivo é compreender, de forma progressiva, como automatizar a validação, construção e entrega de código utilizando um pipeline.

## Estrutura 
github/
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── ci-cd.yml
│
├── tests/
│   ├── test_app.py
│   └── test_pipeline.py
│
├── app.py
├── README.md
└── requirements.txt

## Principais arquivos

**app.py:** Contém a aplicação Python utilizada nos exemplos.

**tests/:** Contém os testes automatizados executados pelo pytest.

**requirements.txt:** Contém as dependências Python necessárias para execução do projeto.

**.github/workflows/:** Contém os workflows utilizados pelo GitHub Actions para automatizar os processos de CI/CD.