import nltk
from deep_translator import GoogleTranslator


def quantidade_verbo(sentenca):
    traduzir_ingles = \
        GoogleTranslator(source='portuguese', target='english').translate(sentenca)
    tokens = nltk.word_tokenize(traduzir_ingles)
    tagged = nltk.pos_tag(tokens)
    qtd_verbo = 0
    for tag in tagged:
        if tag[1][0] == 'V':
            qtd_verbo = qtd_verbo + 1
    if qtd_verbo in [0, 1]:
        complex_verbo = 'Ensino Fundamental 1'
    else:
        complex_verbo = 'Ensino Médio'
    return complex_verbo


def quantidade_modificacoes(lista_modificacoes):
    qtd_mudanca = len(lista_modificacoes)
    if qtd_mudanca in [1, 2]:
        complex_mudanca = 'Ensino Fundamental 1'
    elif qtd_mudanca in [3]:
        complex_mudanca = 'Ensino Fundamental 2'
    elif qtd_mudanca in [4]:
        complex_mudanca = 'Ensino Fundamental 3'
    elif qtd_mudanca in [5]:
        complex_mudanca = 'Ensino Médio'
    else:
        complex_mudanca = 'Ensino Superior'
    return complex_mudanca
