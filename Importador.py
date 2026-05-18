import csv
import pandas as pd


class Importador:

    def importar_csv(self, nome_arquivo):

        x = []

        y = []

        with open(
            nome_arquivo,
            newline="",
            encoding="utf-8"
        ) as arquivo:

            leitor = csv.reader(arquivo)

            # pula cabeçalho
            next(leitor)

            for linha in leitor:

                x.append(linha[0])

                y.append(int(linha[1]))

        return x, y

    def importar_excel (self, nome_arquivo):

        arquivo = pd.read_excel(nome_arquivo)

        x = arquivo.iloc[:,0].tolist()
        y = arquivo.iloc[:,1].astype(float).tolist()
        return x, y