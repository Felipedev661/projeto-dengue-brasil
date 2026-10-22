# Apresentação Final do Projeto — Dengue no Brasil

**Projeto de parceria EBAC/Semantix**

## 1. Objetivo

Desenvolver uma análise exploratória de dados públicos sobre dengue no Brasil, buscando identificar padrões temporais e observar a distribuição dos registros por classificação. O projeto demonstra como a análise de dados pode contribuir para a compreensão do cenário epidemiológico e apoiar o planejamento de ações preventivas.

## 2. Fonte de dados

Foram utilizados arquivos anuais do Sistema de Informação de Agravos de Notificação (SINAN), referentes a 2023, 2024 e 2025, disponibilizados pelo Ministério da Saúde.

Fonte oficial: https://dadosabertos.saude.gov.br/dataset/arboviroses-dengue

## 3. Ferramentas utilizadas

- **Python e pandas:** processamento, filtragem e agregação dos dados.
- **Google Colab:** execução do código de análise.
- **Google Sheets:** apoio à organização dos dados.
- **Looker Studio:** criação do painel interativo.
- **GitHub:** versionamento e documentação do projeto.

## 4. Entregáveis

O repositório contém:

- Definição do problema e justificativa.
- Fontes de dados e metodologia.
- Script de processamento em Python.
- Notebook executável no Google Colab.
- Arquivo CSV com os resultados agregados.
- Documento com resultados e limitações.
- Painel interativo no Looker Studio.

## 5. Resultados preliminares

O processamento gerou uma tabela agregada com **111 linhas e 4 colunas**, totalizando **8.865.439 registros contabilizados** nos arquivos analisados após a aplicação dos filtros definidos.

O painel permite explorar os registros por mês, ano e classificação, com filtros interativos para facilitar a visualização.

**Importante:** esse total representa registros contabilizados, não necessariamente casos únicos de dengue ou pessoas distintas.

## 6. Limitações e cuidados metodológicos

Os resultados são exploratórios e precisam de validações adicionais antes de sustentar conclusões epidemiológicas definitivas.

Entre os pontos que exigem atenção estão:

- A comparabilidade dos volumes de registros entre os anos.
- A possível sobreposição de registros entre os arquivos anuais.
- A confirmação dos códigos de classificação utilizados no dicionário oficial.
- A necessidade de validar os critérios de inclusão e a interpretação dos resultados.

Por esses motivos, as diferenças observadas entre os anos não devem ser interpretadas automaticamente como variações reais na incidência da dengue.

## 7. Conclusão

O projeto demonstra a aplicação de ferramentas de análise de dados para processar, organizar e visualizar informações públicas de saúde. Também destaca a importância de documentar as etapas do trabalho e reconhecer as limitações dos dados antes de formular conclusões.

A análise poderá ser aprimorada com verificações adicionais de qualidade, comparabilidade e duplicidade dos registros.

## 8. Links do projeto

- **Repositório GitHub:** https://github.com/Felipedev661/projeto-dengue-brasil
- **Painel interativo:** https://datastudio.google.com/reporting/bef1930a-9922-4088-858a-9046b04f94c4
- **Fonte oficial dos dados:** https://dadosabertos.saude.gov.br/dataset/arboviroses-dengue
