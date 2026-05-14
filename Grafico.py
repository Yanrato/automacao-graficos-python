import matplotlib.pyplot as plt


from Estatisticas import Estatisticas


class Grafico:

    def __init__(self, xb, yb):

        self.xb = xb
        self.yb = yb

        self.title = ""
        self.xlabel = ""
        self.ylabel = ""

        # objeto de estatísticas
        self.estatisticas = Estatisticas(self.yb)


    def titulo_grafico(self, title):

        self.title = title


    def labels_grafico(self, xlabel, ylabel):

        self.xlabel = xlabel
        self.ylabel = ylabel


    def linha_media(self):

        media = self.estatisticas.media()

        plt.axhline(
            media,
            color="orange",
            linestyle="--",
            label=f"Média: {media:.2f}"
        )

        plt.legend()

    def desvio_padrao(self):

        media = self.estatisticas.media()
        desvio = self.estatisticas.desvio_padrao()

        plt.axhline(
            media + desvio,
            color="purple",
            linestyle=":",
            label=f"Desvio: {media - desvio:.2f}"
        )
        plt.legend()

    def desvio_histograma(self):

        media = self.estatisticas.media()

        desvio = self.estatisticas.desvio_padrao()

        plt.axvline(
            media + desvio,
            color="purple",
            linestyle=":"
        )
        plt.legend()
        plt.axvline(
            media - desvio,
            color="purple",
            linestyle=":"
        )

        plt.legend()

    def maxpoint(self):

        maior = self.estatisticas.maior()

        indice_maior = self.yb.index(maior)

        plt.scatter(
            self.xb[indice_maior],
            maior,
            color="green",
            s=150,
            label=f"Maior: {maior}"
        )

        plt.legend()

    def maxline(self):
        maior = self.estatisticas.maior()
        indice_maior = self.yb.index(maior)

        plt.axhline(
            self.yb[indice_maior],
            color="green",
            linestyle="--",
            label=f"Maior: {maior}"
        )
        plt.legend()

    def minpoint(self):

        menor = self.estatisticas.menor()

        indice_menor = self.yb.index(menor)

        plt.scatter(
            self.xb[indice_menor],
            menor,
            color="red",
            s=150,
            label=f"Menor: {menor}"
        )

        plt.legend()

    def minline(self):
        menor = self.estatisticas.menor()
        indice_menor = self.yb.index(menor)

        plt.axhline(
            self.yb[indice_menor],
            color="red",
            linestyle="--",
            label=f"Menor: {menor}"
        )
        plt.legend()

    def gerar_grafico(self, tipo):

        # limpa figura anterior
        plt.clf()

        # ---------------- LINHA ----------------
        match tipo:

            case "1":

                plt.plot(
                    self.xb,
                    self.yb,
                    marker='o'
                )

                plt.grid()

                # valores nos pontos
                for i, valor in enumerate(self.yb):

                    plt.text(
                        self.xb[i],
                        valor + 0.05,
                        str(valor)
                    )

                self.linha_media()
                self.maxpoint()
                self.minpoint()
                self.desvio_padrao()


            # ---------------- BARRAS ----------------
            case "2":

                plt.bar(
                    self.xb,
                    self.yb
                )

                plt.grid()

                # valores nas barras
                for i, valor in enumerate(self.yb):

                    plt.text(
                        i,
                        valor,
                        str(valor)
                    )

                self.linha_media()
                self.maxline()
                self.minline()
                self.desvio_padrao()


            # ---------------- PIZZA ----------------
            case "3":

                def porcentagem(pct):

                    total = sum(self.yb)

                    valor = int(pct * total / 100)

                    return f"{valor} ({pct:.1f}%)"

                plt.pie(
                    self.yb,
                    labels=self.xb,
                    autopct=porcentagem
                )


            # ---------------- HISTOGRAMA ----------------
            case "4":

                counts, bins, patches = plt.hist(self.yb)

                plt.grid()

                # frequência nas barras
                for i in range(len(counts)):

                    plt.text(
                        bins[i],
                        counts[i],
                        str(int(counts[i]))
                    )

                media = self.estatisticas.media()

                plt.axvline(
                    media,
                    color="orange",
                    linestyle="--",
                    label=f"Média: {media:.2f}"
                )

                plt.legend()

                self.desvio_histograma()


            # ---------------- DISPERSÃO ----------------
            case "5":

                plt.scatter(
                    self.xb,
                    self.yb
                )

                plt.grid()

                # valores nos pontos
                for i, valor in enumerate(self.yb):

                    plt.text(
                        self.xb[i],
                        valor + 0.05,
                        str(valor)
                    )

                self.linha_media()
                self.maxpoint()
                self.minpoint()
                self.desvio_padrao()


            # ---------------- INVÁLIDO ----------------
            case _:

                print("Opção inválida")
                return


        # configurações gerais
        plt.title(self.title)

        plt.xlabel(self.xlabel)

        plt.ylabel(self.ylabel)


    def salvar_imagempng(self, nome):

        plt.savefig(
            f"{nome}.png",
            bbox_inches="tight"
        )


    def mostrar(self):

        plt.show()