# Dengue no Brasil: problema e justificativa

## 1. Problema

A dengue representa um desafio para a saúde pública brasileira, com ocorrência de surtos e variações no número de registros ao longo do tempo e entre regiões. Compreender esses padrões pode ajudar a identificar períodos de maior ocorrência e orientar ações preventivas.

O problema investigado neste projeto é: **quais padrões temporais podem ser identificados nos registros de dengue no Brasil entre 2023 e 2025, e como a análise exploratória desses dados pode contribuir para o planejamento de ações de prevenção?**

## 2. Justificativa

A análise de dados epidemiológicos permite transformar grandes volumes de registros em informações que facilitam a compreensão da distribuição temporal da doença. A identificação de meses com maior concentração de registros pode apoiar o planejamento de campanhas de conscientização e de medidas de controle do mosquito transmissor.

O projeto utiliza dados públicos do Sistema de Informação de Agravos de Notificação (SINAN), disponibilizados pelo Ministério da Saúde, e ferramentas de análise de dados, como Python, pandas e Looker Studio.

## 3. Objetivo geral

Realizar uma análise exploratória dos registros de dengue no Brasil, com foco nos padrões mensais e nas classificações dos casos registrados.

## 4. Objetivos específicos

- Organizar e preparar os dados públicos de dengue.
- Examinar a distribuição mensal dos registros.
- Explorar as classificações finais disponíveis na base.
- Construir visualizações interativas para facilitar a interpretação dos dados.
- Documentar as etapas, limitações e resultados da análise.

## 5. Fonte dos dados

Os dados são provenientes do portal de dados abertos do Ministério da Saúde, na seção referente à dengue e às arboviroses:

https://dadosabertos.saude.gov.br/dataset/arboviroses-dengue

Foram utilizados arquivos anuais do SINAN referentes a 2023, 2024 e 2025.

## 6. Limitações iniciais

Os resultados apresentados nesta etapa devem ser interpretados como contagens de registros filtrados, e não necessariamente como número de pessoas únicas ou casos confirmados sem duplicidade. Os arquivos anuais ainda precisam ser avaliados quanto à sobreposição de registros e à comparabilidade entre períodos.

Além disso, os códigos das classificações e dos critérios utilizados no filtro devem ser interpretados conforme a documentação oficial do SINAN. Portanto, os gráficos iniciais são exploratórios e não devem ser utilizados isoladamente para estabelecer conclusões epidemiológicas definitivas.

## 7. Resultado esperado

Espera-se produzir uma análise exploratória documentada, acompanhada de gráficos e de um painel interativo, que ajude a visualizar a distribuição temporal dos registros de dengue e demonstre a aplicação de técnicas de análise de dados em uma questão relevante de saúde pública.
