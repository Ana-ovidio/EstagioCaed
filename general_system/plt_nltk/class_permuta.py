from itertools import permutations


class Permutacoes:

    def __init__(self, tagged=None, oracoes=None):
        self.tagged = tagged
        self.oracoes = oracoes

    def separa_elementos_oracao(self):
        sujeito = []
        predicado = []
        # Separar o sujeito do predicado
        for i, tag in enumerate(self.tagged):
            if tag[1][0] == 'V':
                break
            else:
                sujeito.append(tag[0])

        for j in range(i, len(self.tagged)):
            predicado.append(self.tagged[j][0])
        predicado_concatenado = [' '.join(predicado)]

        # Separar o sujeito principal do aposto
        aposto = []
        sujeito_principal = []

        qnt_virgulas = 0
        posicao_virgulas = []
        for i, tag in enumerate(self.tagged):
            if tag[0] == ',':
                qnt_virgulas = qnt_virgulas + 1
                posicao_virgulas.append(i)

        if len(posicao_virgulas) == 1:
            aposto = sujeito[:posicao_virgulas[0]]
            sujeito_principal = sujeito[posicao_virgulas[0] + 1:]
        elif len(posicao_virgulas) == 2:
            aposto = sujeito[posicao_virgulas[0] + 1:posicao_virgulas[1]]
            sujeito_principal = sujeito[:posicao_virgulas[0]] + sujeito[posicao_virgulas[1] + 1:]
        else:
            sujeito_principal = sujeito
        suj = []  # sujeito em string
        aposto_suj = []  # aposto em string

        suj.append(' '.join(sujeito_principal))
        if len(aposto) != 0:
            aposto_suj.append(' '.join(aposto))
        else:
            aposto_suj.append(None)
        return suj[0], aposto_suj[0], predicado_concatenado

    def permutacao_sujeito_aposto(self, suj, aposto=None):

        if aposto is not None:
            primeira_permutacao = list(permutations([suj, aposto]))

            inserir_virgula = []
            permutacoes_string = []

            # Tranformar tuplas em lista para permitir modificação
            permutacoes = []
            for tupla in primeira_permutacao:
                permutacoes.append(list(tupla))

            for i, permutacao in enumerate(permutacoes):
                # A primeira sentenca da permutação começa com letra maiúscula
                if permutacao[0][0] == permutacao[0][0].upper():
                    pass
                else:
                    lista_palavras = list(permutacao[0])
                    lista_palavras[0] = lista_palavras[0].upper()
                    permutacao[0] = ''.join(lista_palavras)
                # A segunda sentenca da permutação começa com letra maiúscula
                if permutacao[1][0] == permutacao[1][0].upper():
                    lista_palavras = list(permutacao[1])
                    lista_palavras[0] = lista_palavras[0].lower()
                    permutacao[1] = ''.join(lista_palavras)
                else:
                    pass

            # Concatenar strings permutadas
            permutacoes_concatenadas = []
            for i in range(len(permutacoes)):
                permutacoes_concatenadas.append(' '.join(permutacoes[i]))

        else:
            permutacoes_concatenadas = [suj]

        return permutacoes_concatenadas

    def permutacao_sujeito_predicado(self, sujeitos, predicado):


        primeira_permutacao = []
        for sujeito in sujeitos:
            primeira_permutacao.append(list(permutations([sujeito, predicado[0]])))

        # Tranformar tuplas em lista para permitir modificação
        permutacoes = []
        for lista in primeira_permutacao:
            for tupla in lista:
                permutacoes.append(list(tupla))
            for i, permutacao in enumerate(permutacoes):
                # A primeira sentenca da permutação começa com letra maiúscula
                if permutacao[0][0] == permutacao[0][0].upper():
                    pass
                else:
                    lista_palavras = list(permutacao[0])
                    lista_palavras[0] = lista_palavras[0].upper()
                    permutacao[0] = ''.join(lista_palavras)
                # A segunda sentenca da permutação começa com letra maiúscula
                if permutacao[1][0] == permutacao[1][0].upper():
                    lista_palavras = list(permutacao[1])
                    lista_palavras[0] = lista_palavras[0].lower()
                    permutacao[1] = ''.join(lista_palavras)
                else:
                    pass

            # Concatenar strings permutadas
            permutacoes_concatenadas = []
            for i in range(len(permutacoes)):

                if permutacoes[i][-1][-1] == ',':
                    frase_com_virgula = list(permutacoes[i][-1])
                    frase_com_virgula[-1] = '.'
                    permutacoes[i][-1] = ''.join(frase_com_virgula)
                permutacoes_concatenadas.append(' '.join(permutacoes[i]))

        return permutacoes_concatenadas

    def permutacao_oracoes(self):

        primeira_permutacao = list(permutations(self.oracoes))

        # Tranformar tuplas em lista para permitir modificação
        permutacoes = []
        for tupla in primeira_permutacao:
            permutacoes.append(list(tupla))
        permutacoes_concatenadas = []

        # Concatenar as strings
        for permutacao in permutacoes:
            if permutacao[0][0] == permutacao[0][0].upper():
                pass
            else:
                primeira_string = list(permutacao[0])
                primeira_string[0] = primeira_string[0].upper()
                permutacao[0] = ''.join(primeira_string)

                segunda_string = list(permutacao[1])
                segunda_string[0] = segunda_string[0].lower()
                permutacao[1] = ''.join(segunda_string)

            permutacoes_concatenadas.append(' '.join(permutacao))

        return permutacoes_concatenadas
