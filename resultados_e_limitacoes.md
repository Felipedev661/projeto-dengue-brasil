# Resultados preliminares e limitações

## 1. Visão geral

Este projeto realiza uma análise exploratória de dados públicos de dengue do Sistema de Informação de Agravos de Notificação (SINAN), referentes aos arquivos anuais de 2023, 2024 e 2025.

O processamento selecionou registros com classificações finais codificadas como `10`, `11` ou `12`, critérios `1` ou `2` e datas válidas de início dos sintomas.

## 2. Resumo do processamento

A tabela agregada gerada pelo código apresentou:

- **111 linhas** de combinações entre ano, mês e classificação.
- **4 colunas:** ano, mês, classificação e quantidade de registros.
- **8.865.439 registros contabilizados** no conjunto agregado.

Esse total corresponde à soma das contagens produzidas a partir dos três arquivos anuais. Ele não deve ser interpretado como número de pessoas únicas nem como total definitivo de casos confirmados.

## 3. Distribuição por ano dos sintomas

As contagens preliminares obtidas foram:

| Ano de início dos sintomas | Registros contabilizados |
|---|---:|
| 2023 | 1.422.512 |
| 2024 | 5.978.688 |
| 2025 | 1.461.707 |
| 2026 | 2.532 |
| **Total** | **8.865.439** |

O ano de 2026 aparece porque há registros com datas de início dos sintomas nesse ano, embora os arquivos utilizados tenham sido identificados como bases anuais de 2023, 2024 e 2025.

Esses valores são preliminares e podem incluir registros sobrepostos entre arquivos. Portanto, não permitem concluir, por si só, que houve aumento ou redução equivalente no número real de casos de dengue.

## 4. Classificações registradas

Na agregação, foram mantidos os códigos de classificação final `10`, `11` e `12`.

A contagem observada foi:

| Código | Interpretação |
|---|---|
| 10 | A confirmar no dicionário oficial do SINAN |
| 11 | A confirmar no dicionário oficial do SINAN |
| 12 | A confirmar no dicionário oficial do SINAN |

A interpretação definitiva desses códigos deverá ser conferida na documentação oficial correspondente à base utilizada.

## 5. Sazonalidade

Os gráficos mensais permitem visualizar a distribuição dos registros ao longo do ano e identificar períodos com maior concentração de contagens.

Entretanto, a comparação entre anos deve ser feita com cautela. Antes de interpretar diferenças como tendências epidemiológicas, será necessário verificar a sobreposição entre arquivos, a cobertura temporal e a comparabilidade dos registros.

## 6. Limitações identificadas

- **Possível sobreposição entre arquivos:** as bases anuais foram agregadas sem uma deduplicação definitiva entre arquivos.
- **Contagens de registros:** os totais não representam necessariamente indivíduos únicos.
- **Identificação de duplicidades:** não foi possível confirmar a ausência de duplicidades apenas com a variável `NDUPLIC_N`.
- **Interpretação dos códigos:** os códigos de classificação e de critério precisam ser validados no dicionário oficial.
- **Cobertura temporal:** há registros associados a anos adjacentes, incluindo 2026.
- **Ausência de denominadores populacionais:** as contagens absolutas, isoladamente, não permitem comparar risco ou incidência entre populações de tamanhos diferentes.

## 7. Conclusão preliminar

O projeto demonstra um fluxo de processamento de dados públicos utilizando Python e pandas, com agregação mensal e visualização no Looker Studio.

Os resultados devem ser tratados como exploratórios. Uma conclusão epidemiológica mais robusta dependerá da validação dos códigos, da avaliação da sobreposição entre arquivos e da definição de uma metodologia consistente para comparação temporal.

## 8. Próximas melhorias

1. Consultar o dicionário oficial do SINAN para validar os códigos utilizados.
2. Investigar a sobreposição de registros entre os arquivos anuais.
3. Definir e documentar uma estratégia de deduplicação apropriada.
4. Revisar os gráficos após essas verificações.
5. Registrar no painel e no relatório as limitações metodológicas.
