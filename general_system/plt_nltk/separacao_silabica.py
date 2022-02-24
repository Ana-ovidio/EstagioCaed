import nltk


class Canonicidade():
    def __init__(self, sentenca):
        self.sentenca = sentenca

    def tokenizacao(self):
        tokens = nltk.word_tokenize(self.sentenca)
        if '.' in tokens:
            tokens.remove('.')

        return tokens

    def separacao_silabica(self, tokens):

        lista_vogais = ['a', 'e', 'i', 'o', 'u']
        palavras_canonicas = []

        for token in tokens:
            count = 0
            tamanho_palavra = len(token)

            if tamanho_palavra % 2 == 0:
                silabas = []
                for i in range(0, len(token), 2):
                    j = i + 2
                    silabas.append(token[i:j])
                    i = j

                for silaba in silabas:
                    if ((silaba[0] not in lista_vogais) and
                            (silaba[1] in lista_vogais)):
                        count = count + 1
                    else:
                        break

                if count == tamanho_palavra / 2:
                    palavras_canonicas.append(token)
                else:
                    pass
            else:
                pass

        return palavras_canonicas

    def ver_palavras_canonicas(self):

        tokens = self.tokenizacao()
        palavras_canonicas = self.separacao_silabica(tokens)

        if len(palavras_canonicas) == 0:
            palavras_canonicas = 'Não há palavras canônicas na sentença.'
        else:
            pass

        return palavras_canonicas


sentenca = 'A menina estava com a cabeça na janela'
cano = Canonicidade(sentenca)
palavras_canonicas = cano.ver_palavras_canonicas()
print(palavras_canonicas)
