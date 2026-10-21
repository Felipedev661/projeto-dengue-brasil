# Dengue no Brasil — Análise Epidemiológica

## 1. Sobre o projeto

Este projeto realiza uma análise exploratória de dados públicos de dengue no Brasil, utilizando Python, pandas e Looker Studio. O objetivo é organizar os registros, explorar padrões temporais e apresentar informações por meio de visualizações.

## 2. Problema de negócio

A dengue representa um desafio para a saúde pública brasileira. Compreender a distribuição temporal dos registros e as classificações dos casos pode ajudar a identificar períodos de maior concentração e apoiar o planejamento de ações preventivas.

## 3. Objetivo

Analisar registros públicos de dengue referentes a 2023, 2024 e 2025, explorando a distribuição mensal, as classificações registradas e as limitações dos dados disponíveis.

## 4. Fonte dos dados

Os dados foram obtidos no Portal de Dados Abertos do SUS, por meio dos arquivos anuais do Sistema de Informação de Agravos de Notificação (SINAN).

Fonte oficial: https://dadosabertos.saude.gov.br/dataset/arboviroses-dengue

## 5. Ferramentas utilizadas

- Python
- pandas
- Google Colab
- Looker Studio
- GitHub

## 6. Metodologia

1. Obtenção dos arquivos públicos anuais.
2. Leitura dos arquivos CSV compactados.
3. Seleção preliminar dos registros com classificações 10, 11 e 12 e critérios 1 e 2.
4. Conversão das datas de início dos sintomas.
5. Agrupamento dos registros por ano, mês e classificação.
6. Exploração dos resultados e elaboração de visualizações.
7. Documentação das limitações metodológicas.

## 7. Estrutura do repositório

- `problema_e_justificativa.md`: problema investigado, justificativa e objetivos.
- `fontes_e_metodologia.md`: fontes de dados e procedimentos utilizados.
- `processamento_dengue.py`: código de processamento dos dados.
- `resultados_e_limitações.md`: resultados preliminares e limitações identificadas.
- `README.md`: apresentação geral do projeto.

## 8. Limitações importantes

Os números apresentados representam registros contabilizados após os filtros aplicados, e não necessariamente pessoas únicas ou casos confirmados e deduplicados.

A combinação dos arquivos anuais pode incluir registros repetidos entre bases. A variável de possível duplicidade também não foi suficiente para confirmar a ausência de duplicatas.

Além disso, diferenças no volume dos registros entre os anos exigem validações adicionais antes de realizar comparações epidemiológicas definitivas.

Portanto, os resultados devem ser interpretados como exploratórios, e não como estimativas oficiais do total de pessoas infectadas.

## 9. Próximas etapas

- Validar os códigos de classificação com o dicionário oficial do SINAN.
- Investigar a duplicidade entre arquivos anuais.
- Refinar as comparações temporais.
- Finalizar o painel no Looker Studio.
- Registrar as conclusões após a validação dos dados.

## 10. Status

Projeto em desenvolvimento — análise exploratória e documentação preliminar.
