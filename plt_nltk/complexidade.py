import nltk
from deep_translator import GoogleTranslator


class Complexidade():
    def __init__(self, sentenca, modificacoes, opcoes_mudanca):
        self.sentenca = sentenca
        self.modificacoes = modificacoes
        self.opcoes_mudancas = opcoes_mudanca
        self.niveis_complexidade = [['Ensino Fundamental 1', 0],
                                    ['Ensino Fundamental 2', 1],
                                    ['Ensino Fundamental 3', 2],
                                    ['Ensino Medio', 3],
                                    ['Ensino Superior', 4]]

    def quantidade_verbo(self):
        traduzir_ingles = \
            GoogleTranslator(source='portuguese', target='english').translate(self.sentenca)
        tokens = nltk.word_tokenize(traduzir_ingles)
        tagged = nltk.pos_tag(tokens)
        qtd_verbo = 0
        for tag in tagged:
            if tag[1][0] == 'V':
                qtd_verbo = qtd_verbo + 1
        if qtd_verbo in [0, 1]:
            complex_verbo = self.niveis_complexidade[0]
        else:
            complex_verbo = self.niveis_complexidade[3]
        return complex_verbo[1]

    def quantidade_modificacoes(self):
        qtd_mudanca = len(self.modificacoes)
        if qtd_mudanca in [1, 2]:
            complex_mudanca = self.niveis_complexidade[0]
        elif qtd_mudanca in [3]:
            complex_mudanca = self.niveis_complexidade[1]
        elif qtd_mudanca in [4]:
            complex_mudanca = self.niveis_complexidade[2]
        elif qtd_mudanca in [5]:
            complex_mudanca = self.niveis_complexidade[3]
        else:
            complex_mudanca = self.niveis_complexidade[4]
        return complex_mudanca[1]

    def niveis_escolha(self):
        dificuldade_escolha = {self.opcoes_mudancas[0]: self.niveis_complexidade[1][1],
                               self.opcoes_mudancas[1]: self.niveis_complexidade[0][1],
                               self.opcoes_mudancas[2]: self.niveis_complexidade[3][1],
                               self.opcoes_mudancas[3]: self.niveis_complexidade[3][1],
                               self.opcoes_mudancas[4]: self.niveis_complexidade[4][1],
                               self.opcoes_mudancas[5]: self.niveis_complexidade[2][1]}
        complexidades = []
        for modificacao in self.modificacoes:
            if modificacao in list(dificuldade_escolha.keys()):
                complexidades.append(dificuldade_escolha[modificacao])

        return max(complexidades)

    def define_complexidade(self):
        verbo = self.quantidade_verbo()
        mudancas = self.quantidade_modificacoes()
        escolhas = self.niveis_escolha()

        # Lista com vários índices respectivos às complexidades
        niveis = [verbo, mudancas, escolhas]

        for i in range(len(self.niveis_complexidade)):
            if self.niveis_complexidade[i][1] == max(niveis):
                nivel_ensino = self.niveis_complexidade[i][0]

        return nivel_ensino
