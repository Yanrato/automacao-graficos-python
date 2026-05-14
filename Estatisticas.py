import math

class Estatisticas:

    def __init__(self, dados):

        self.dados = dados


    def media(self):

        return sum(self.dados) / len(self.dados)

    def desvio_padrao(self):
        media = self.media()
        variance = sum(
            (x-media)**2 for x in self.dados
        ) / len(self.dados)
        return math.sqrt(variance)

    def maior(self):

        return max(self.dados)


    def menor(self):

        return min(self.dados)


    def soma(self):

        return sum(self.dados)