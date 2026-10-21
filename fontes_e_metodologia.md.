# Fontes de dados e metodologia

## 1. Fonte de dados

O projeto utiliza dados públicos sobre dengue disponibilizados pelo Ministério da Saúde por meio do Sistema de Informação de Agravos de Notificação (SINAN).

**Portal oficial:**  
https://dadosabertos.saude.gov.br/dataset/arboviroses-dengue

Foram utilizados arquivos anuais referentes a 2023, 2024 e 2025:

- `DENGBR23.csv.zip`
- `DENGBR24.csv.zip`
- `DENGBR25.csv.zip`

## 2. Ferramentas utilizadas

- **Python:** processamento e análise dos dados.
- **pandas:** leitura, filtragem, agrupamento e sumarização dos registros.
- **Google Colab:** ambiente de execução dos códigos.
- **Looker Studio:** criação de visualizações e painel interativo.
- **GitHub:** versionamento e documentação do projeto.

## 3. Preparação e processamento

Os arquivos foram lidos diretamente dos arquivos ZIP, utilizando a codificação `latin1` e o separador por vírgulas.

Para reduzir o consumo de memória, os dados foram processados em blocos de 100.000 linhas.

Foram selecionadas as colunas necessárias à análise, incluindo:

- `DT_SIN_PRI`: data de início dos sintomas.
- `CLASSI_FIN`: classificação final.
- `CRITERIO`: critério de confirmação registrado na base.

## 4. Filtros aplicados

Na etapa exploratória, foram selecionados registros com:

- `CLASSI_FIN` igual a `10`, `11` ou `12`.
- `CRITERIO` igual a `1` ou `2`.
- Data de início dos sintomas válida.

Os códigos foram mantidos como valores categóricos durante o processamento. Sua interpretação definitiva deve seguir o dicionário oficial do SINAN.

## 5. Agregação mensal

A data de início dos sintomas foi convertida para o formato de data. Em seguida, foram extraídos o ano e o mês.

Os registros foram agrupados por:

- Ano de início dos sintomas.
- Mês de início dos sintomas.
- Classificação final.

A quantidade de linhas de cada grupo foi contabilizada e exportada para o arquivo `dengue_resumo_mensal.csv`.

## 6. Verificações realizadas

Foram verificadas as dimensões da base resumida, a presença de valores ausentes em campos relevantes e os valores disponíveis na variável `NDUPLIC_N`.

A base resumida apresentou 111 linhas e quatro colunas. Não foram encontradas linhas duplicadas dentro desse resumo agregado.

**Importante:** a ausência de linhas duplicadas no resumo não comprova que não existam registros repetidos nas bases originais. Os arquivos anuais foram combinados sem uma deduplicação definitiva por identificador de caso.

## 7. Limitações metodológicas

Os resultados representam contagens de registros que atenderam aos filtros aplicados, e não necessariamente pessoas únicas ou casos confirmados sem duplicidade.

Os arquivos anuais podem conter registros referentes a anos adjacentes ou informações sobrepostas. Por isso, comparações entre anos devem ser interpretadas com cautela até que a comparabilidade e a possível sobreposição entre as bases sejam verificadas.

O painel produzido nesta etapa possui finalidade exploratória e não substitui estatísticas epidemiológicas oficiais.

## 8. Produto da etapa

O processamento gera uma tabela mensal resumida, destinada à construção de gráficos e tabelas no Looker Studio.

O código de processamento e as limitações identificadas devem ser documentados para permitir a reprodução e a avaliação dos resultados.
