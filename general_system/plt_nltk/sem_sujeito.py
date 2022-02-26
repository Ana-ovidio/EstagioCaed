import nltk
from deep_translator import GoogleTranslator
from plt_nltk.class_permuta import Permutacoes


def tokenizacao(traduzir_ingles):
    tokens = nltk.word_tokenize(traduzir_ingles)
    # Lista de tuplas cujos elementos são respectivamente a palavra e sua morfologia
    tagged = nltk.pos_tag(tokens)

    return tagged


def separa_oracoes(tagged):
    primeira_oracao = []

    for i in range(1, len(tagged)):
        if (tagged[i][1][0] == 'V') and (tagged[i - 1][1][0] == 'V'):
            primeira_oracao.append(tagged[i - 1][0])
            primeira_oracao.append(tagged[i][0])

            primeiro_verbo = tagged[i - 1]
            segundo_verbo = tagged[i]

            tagged.remove(primeiro_verbo)
            tagged.remove(segundo_verbo)
            break

    segunda_oracao = [tagged[i][0] for i in range(len(tagged))]

    primeira_oracao = ' '.join(primeira_oracao)
    segunda_oracao = ' '.join(segunda_oracao)

    oracoes = [primeira_oracao, segunda_oracao]

    return oracoes


def permutacao_oracoes(oracoes):
    pe = Permutacoes(oracoes=oracoes)
    permutacoes = pe.permutacao_oracoes()
    for i, permutacao in enumerate(permutacoes):
        permutacao = \
            GoogleTranslator(source='english', target='portuguese').translate(permutacao)
        permutacoes[i] = permutacao
    return permutacoes


def integra_funcoes(sentenca):
    traduzir_ingles = \
        GoogleTranslator(source='portuguese', target='english').translate(sentenca)
    tagged = tokenizacao(traduzir_ingles)
    oracoes = separa_oracoes(tagged)
    permutacoes = permutacao_oracoes(oracoes)
    return permutacoes
