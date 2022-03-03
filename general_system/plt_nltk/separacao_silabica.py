import nltk

def tokenizacao(sentenca):
    tokens = nltk.word_tokenize(sentenca)
    if '.' in tokens:
        tokens.remove('.')

    return tokens


def separacao_silabica(tokens):
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


def integra_funcoes (sentenca):
    tokens = tokenizacao(sentenca)
    palavras_canonicas = separacao_silabica(tokens)

    if len(palavras_canonicas) == 0:
        palavras_canonicas = ['Não há palavras canônicas na sentença.']
    else:
        pass

    return palavras_canonicas




