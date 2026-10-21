import zipfile
from collections import Counter

import pandas as pd

# Arquivos públicos do SINAN referentes a 2023, 2024 e 2025.
ARQUIVOS = {
    2023: "/content/DENGBR23.csv.zip",
    2024: "/content/DENGBR24.csv.zip",
    2025: "/content/DENGBR25.csv.zip",
}

COLUNAS = ["DT_SIN_PRI", "CLASSI_FIN", "CRITERIO"]
CLASSIFICACOES = ["10", "11", "12"]
CRITERIOS = ["1", "2"]
TAMANHO_BLOCO = 100_000


def processar_arquivos():
    """Gera contagens mensais por ano de sintomas e classificação."""
    contagens = Counter()

    for ano_arquivo, caminho in ARQUIVOS.items():
        print(f"Processando arquivo de {ano_arquivo}...")

        with zipfile.ZipFile(caminho) as arquivo_zip:
            nome_csv = arquivo_zip.namelist()[0]

            with arquivo_zip.open(nome_csv) as arquivo_csv:
                blocos = pd.read_csv(
                    arquivo_csv,
                    sep=",",
                    encoding="latin1",
                    usecols=COLUNAS,
                    dtype=str,
                    chunksize=TAMANHO_BLOCO,
                )

                for bloco in blocos:
                    filtro = (
                        bloco["CLASSI_FIN"].isin(CLASSIFICACOES)
                        & bloco["CRITERIO"].isin(CRITERIOS)
                    )

                    dados = bloco.loc[filtro].copy()
                    dados["Data"] = pd.to_datetime(
                        dados["DT_SIN_PRI"],
                        errors="coerce",
                    )
                    dados = dados.dropna(subset=["Data"])

                    dados["Ano"] = dados["Data"].dt.year
                    dados["Mes"] = dados["Data"].dt.month

                    agrupado = dados.groupby(
                        ["Ano", "Mes", "CLASSI_FIN"]
                    ).size()

                    for chave, quantidade in agrupado.items():
                        contagens[chave] += int(quantidade)

    linhas = [
        {
            "Ano": ano,
            "Mes": mes,
            "Classificacao": classificacao,
            "Quantidade_registros": quantidade,
        }
        for (ano, mes, classificacao), quantidade in contagens.items()
    ]

    resumo = pd.DataFrame(linhas)

    if not resumo.empty:
        resumo = resumo.sort_values(
            ["Ano", "Mes", "Classificacao"]
        )

    destino = "/content/dengue_resumo_mensal.csv"
    resumo.to_csv(
        destino,
        index=False,
        encoding="utf-8-sig",
    )

    print(f"\nArquivo gerado: {destino}")
    print(f"Dimensões do resumo: {resumo.shape}")
    print("\nTotal de registros contabilizados por ano:")
    print(resumo.groupby("Ano")["Quantidade_registros"].sum())

    return resumo


if __name__ == "__main__":
    base_resumida = processar_arquivos()
    print("\nPrévia da base resumida:")
    print(base_resumida.head(10).to_string(index=False))
