from Valores import Valores
from Grafico import Grafico
from Estatisticas import Estatisticas
from Excel import Excel


print("=== Sistema de Gráficos ===")


def main():

    while True:

        # título
        titulo = input("Digite o título do gráfico: ")

        # tipo de gráfico
        tipo = input('''
Escolha o gráfico:

1 - Linha
2 - Barras
3 - Pizza
4 - Histograma
5 - Dispersão

Digite:
''')

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

                continue


        # cria objetos
        v1 = Valores(x, y)

        g1 = Grafico(v1.valorx, v1.valory)

        g1.titulo_grafico(titulo)


        # labels só para gráficos com eixo
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


        # salvar imagem
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

            print("Imagem salva com sucesso!")

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

            print("Excel exportado com sucesso!")
        # mostra gráfico
        g1.mostrar()


        # continuar programa
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