from Valores import Valores
from Grafico import Grafico
from Estatisticas import Estatisticas
from Excel import Excel
from Importador import Importador


print("=== Sistema de Gráficos ===")


def escolher_modo():

    modo = input("""
1 - Inserir dados manualmente
2 - Importar CSV
3 - Importar Excel

Digite:
""")

    while modo not in ["1", "2", "3"]:

        print("Valor incorreto!")

        modo = input("""
1 - Inserir dados manualmente
2 - Importar CSV
3 - Importar Excel

Digite:
""")

    return modo


def tipo_grafico():

    tipo = input('''
Escolha o gráfico:

1 - Linha
2 - Barras
3 - Pizza
4 - Histograma
5 - Dispersão

Digite:
''')

    while tipo not in ["1", "2", "3", "4", "5"]:

        print("Tipo inválido!")

        tipo = input("Digite novamente: ")

    return tipo


def obter_dados_manualmente(tipo):

    # HISTOGRAMA
    if tipo == "4":

        yinput = input(
            "Digite os dados do histograma separados por vírgula:\n"
        )

        x = []

        y = [int(i.strip()) for i in yinput.split(",")]

    # PIZZA
    elif tipo == "3":

        xinput = input(
            "Digite os nomes das fatias separados por vírgula:\n"
        )

        yinput = input(
            "Digite os valores das fatias separados por vírgula:\n"
        )

        x = xinput.split(",")

        y = [int(i.strip()) for i in yinput.split(",")]

    # LINHA, BARRAS E DISPERSÃO
    else:

        xinput = input(
            "Digite os valores de X separados por vírgula:\n"
        )

        yinput = input(
            "Digite os valores de Y separados por vírgula:\n"
        )

        x = xinput.split(",")

        y = [int(i.strip()) for i in yinput.split(",")]

        # valida tamanho
        if len(x) != len(y):

            print(
                "Erro: X e Y precisam ter o mesmo tamanho."
            )

            return None, None

    return x, y


def importar_csv():

    nome_csv = input(
        "Digite o nome do arquivo CSV: "
    )

    importador = Importador()

    x, y = importador.importar_csv(nome_csv)

    return x, y

def importar_excel():

    nome_excel = input(
        "Digite o nome do arquivo Excel: "
    )

    importador = Importador()

    x, y = importador.importar_excel(nome_excel)

    return x, y

def main():

    while True:

        modo = escolher_modo()

        titulo = input(
            "Digite o título do gráfico: "
        )

        tipo = tipo_grafico()

        # DADOS
        if modo == "1":

            x, y = obter_dados_manualmente(tipo)

            if x is None:
                continue

        elif modo == "2":

            x, y = importar_csv()


        else:
            x, y = importar_excel()
            
            print(x)
            print(y)

        # cria objetos
        v1 = Valores(x, y)

        g1 = Grafico(
            v1.valorx,
            v1.valory
        )

        g1.titulo_grafico(titulo)

        # labels
        if modo == "1":
            if tipo in ["1", "2", "4", "5"]:
                xlabel = input(
                    "Digite o rótulo do eixo X: "
                )

                ylabel = input(
                     "Digite o rótulo do eixo Y: "
                )

                g1.labels_grafico(
                    xlabel,
                    ylabel
                )

        # gera gráfico
        g1.gerar_grafico(tipo)

        # estatísticas
        e1 = Estatisticas(v1.valory)

        print("\n=== Estatísticas ===")

        print(f"Média: {e1.media():.2f}")

        print(f"Maior: {e1.maior()}")

        print(f"Menor: {e1.menor()}")

        print(f"Soma: {e1.soma()}")

        print(
            f"Desvio padrão: "
            f"{e1.desvio_padrao():.2f}"
        )

        # salvar png
        salvar = input(
            "\nDeseja salvar como PNG? (s/n): "
        )

        while salvar not in ["s", "n"]:

            salvar = input(
                "Resposta inválida. (s/n): "
            )

        if salvar == "s":

            nome = input(
                "Digite o nome do arquivo: "
            )

            g1.salvar_imagempng(nome)

            print(
                "Imagem salva com sucesso!"
            )

        # exportar excel
        excel = input(
            "\nDeseja exportar para Excel? (s/n): "
        )

        while excel not in ["s", "n"]:

            excel = input(
                "Resposta inválida. (s/n): "
            )

        if excel == "s":

            nome_excel = input(
                "Digite o nome do arquivo Excel: "
            )

            exportador = Excel(
                v1.valorx,
                v1.valory,
                e1
            )

            exportador.exportar(nome_excel)

            print(
                "Excel exportado com sucesso!"
            )

        # mostra gráfico
        g1.mostrar()

        # continuar
        continuar = input(
            "\nDeseja criar outro gráfico? (s/n): "
        )

        while continuar not in ["s", "n"]:

            continuar = input(
                "Resposta inválida. (s/n): "
            )

        if continuar == "n":

            print("Programa encerrado.")

            break


main()