class TrocaGenero:
    def __init__(self, genero, tokens):

        self.tokens = tokens
        self.genero = genero
        self.inicio_fem = ['A', 'Uma', 'Alguma', 'Aquela', 'Umas', 'Algumas', 'Aquelas']
        self.inicio_masc = ['O', 'Um', 'Algum', 'Aquele', 'Uns', 'Alguns', 'Aqueles']

    def modifica_elementos_sing(self):
        troca_genero = []

        if self.genero == 'feminino':
            pos_artigo = self.inicio_fem.index(self.tokens[0])
            troca_genero.append(self.inicio_masc[pos_artigo])

            # Trocar o substantivo
            if 'ora' in self.tokens[1]:
                troca_genero.append(self.tokens[1].replace('ora', 'or'))
            # Não há problema esta verificação, pois a string 'ora' já foi verificada
            elif 'a' in self.tokens[1][-1]:
                tamanho_sub = len(self.tokens[1])
                troca_genero.append(self.tokens[1][:tamanho_sub - 1] + 'o')
            elif ('ente', 'esta', 'ante'):
                troca_genero.append(self.tokens[1])

            # Insere verbo
            troca_genero.append(self.tokens[2])

            # Modifica adjetivo
            if self.tokens[3][-1] == 'a':
                tamanho_adj = len(self.tokens[3])
                troca_genero.append(self.tokens[3][:tamanho_adj - 1] + 'o')
            else:
                troca_genero.append(self.tokens[3])

            troca_genero.append('.')
            texto_modificado = ' '.join(troca_genero)

        else:
            pos_artigo = self.inicio_masc.index(self.tokens[0])
            troca_genero.append(self.inicio_fem[pos_artigo])

            # Trocar o substantivo
            if 'or' in self.tokens[1]:
                troca_genero.append(self.tokens[1].replace('or', 'ora'))
            # Não há problema esta verificação, pois a string 'ora' já foi verificada
            elif 'o' in self.tokens[1][-1]:
                tamanho_sub = len(self.tokens[1])
                troca_genero.append(self.tokens[1][:tamanho_sub - 1] + 'a')
            elif ('ente', 'esta', 'ante'):
                troca_genero.append(self.tokens[1])

            # Insere verbo
            troca_genero.append(self.tokens[2])

            # Modifica adjetivo
            if self.tokens[3][-1] == 'o':
                tamanho_adj = len(self.tokens[3])
                troca_genero.append(self.tokens[3][:tamanho_adj - 1] + 'a')
            else:
                troca_genero.append(self.tokens[3])

            texto_modificado = ' '.join(troca_genero)
        return texto_modificado

    # ------------------------------------------------------------------------------

    def modifica_elementos_plural(self):
        troca_genero = []

        if self.genero == 'feminino':
            pos_artigo = self.inicio_fem.index(self.tokens[0])
            troca_genero.append(self.inicio_masc[pos_artigo])

            # Trocar o substantivo
            if self.tokens[1][-4:] == 'oras':
                troca_genero.append(self.tokens[1].replace('oras', 'ores'))

            # Não há problema esta verificação, pois a string 'ora' já foi verificada
            elif self.tokens[1][-2:] == 'as':
                tamanho_sub = len(self.tokens[1])
                troca_genero.append(self.tokens[1][:tamanho_sub - 2] + 'os')

            elif self.tokens[1][-5:] in ['entes', 'estas', 'antes']:
                troca_genero.append(self.tokens[1])

            # Insere verbo
            troca_genero.append(self.tokens[2])

            # Modifica adjetivo
            if self.tokens[3][-2:] == 'as':
                tamanho_adj = len(self.tokens[3])
                troca_genero.append(self.tokens[3][:tamanho_adj - 2] + 'os')
            else:
                troca_genero.append(self.tokens[3])
            texto_modificado = ' '.join(troca_genero)

        # ------
        else:
            pos_artigo = self.inicio_masc.index(self.tokens[0])
            troca_genero.append(self.inicio_fem[pos_artigo])

            # Trocar o substantivo
            if self.tokens[1][-4:] == 'ores':
                troca_genero.append(self.tokens[1].replace('ores', 'oras'))
            elif self.tokens[1][-2:] == 'os':
                tamanho_sub = len(self.tokens[1])
                troca_genero.append(self.tokens[1][:tamanho_sub - 2] + 'as')
            elif self.tokens[1][-5:] in ['entes', 'estas', 'antes']:
                troca_genero.append(self.tokens[1])

            # Insere verbo
            troca_genero.append(self.tokens[2])

            # Modifica adjetivo
            if self.tokens[3][-2:] == 'os':
                tamanho_adj = len(self.tokens[3])
                troca_genero.append(self.tokens[3][:tamanho_adj - 2] + 'as')
            else:
                troca_genero.append(self.tokens[3])

            texto_modificado = ' '.join(troca_genero)

        return texto_modificado