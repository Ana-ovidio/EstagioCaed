import nltk
from deep_translator import GoogleTranslator
from general_system.plt_nltk.class_permuta import Permutacoes


def tokenizacao(traduzir_ingles):
    tokens = nltk.word_tokenize(traduzir_ingles)
    # Lista de tuplas cujos elementos são respectivamente a palavra e sua morfologia
    tagged = nltk.pos_tag(tokens)

    return tagged


def separa_oracoes(tagged):
    primeira_oracao = []
    for i, tag in enumerate(tagged):
        if tag[1][0] == 'N':
            existe_verbo = False
            break
        elif tag[1][0] == 'V':
            existe_verbo = True
            break
        else:
            primeira_oracao.append(tag)

    if existe_verbo == True:
        primeira_oracao.append(tag)
        i = i + 1
        while i != len(tagged) - 1:
            if tagged[i][1][0] == 'V':
                primeira_oracao.append(tagged[i])
                i = i + 1
            else:
                break
        segunda_oracao = tagged[i + 1:]
    else:
        primeira_oracao.append(tag)
        i = i + 1
        while i != len(tagged) - 1:
            print(tagged[i])
            if (tagged[i][1][0] != 'V') and (tagged[i][1] != 'PRP'):
                primeira_oracao.append(tagged[i])
                i = i + 1
            else:
                break
        segunda_oracao = tagged[i:]

    for i, tag in enumerate(primeira_oracao):
        primeira_oracao[i] = tag[0]
    for i, tag in enumerate(segunda_oracao):
        segunda_oracao[i] = tag[0]

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
