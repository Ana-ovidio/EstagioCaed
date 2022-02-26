import nltk
from nltk.corpus import wordnet as wn
from random import choices
from deep_translator import GoogleTranslator


def tokenizacao(traduzir_ingles):
    tokens = nltk.word_tokenize(traduzir_ingles)
    # Lista de tuplas cujos elementos são respectivamente a palavra e sua morfologia
    tagged = nltk.pos_tag(tokens)
    for tag in tagged:
        if tag[1] == 'JJ':
            adjetivo = tag[0]
        else:
            adjetivo = None

    return adjetivo


def sinonimos_antonimos(adjetivo):
    synonyms = []
    antonyms = []

    for syn in wn.synsets(adjetivo):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())

    return synonyms, antonyms


def escolhe_adjetivo(synonyms, antonyms):
    tipo_troca = choices(['synonyms', 'antonyms'])
    tipo_troca

    if (len(antonyms) == 0) and (len(synonyms) != 0):
        novo_adjetivo = choices(synonyms)
    elif (len(synonyms) == 0) and (len(antonyms) != 0):
        novo_adjetivo = choices(antonyms)
    elif (len(antonyms) == 0) and (len(synonyms) != 0):
        novo_adjetivo = None
    elif tipo_troca == 'synonyms':
        novo_adjetivo = choices(synonyms)
    else:
        novo_adjetivo = choices(antonyms)

    return novo_adjetivo


def traduz_sentenca_mod (adjetivo, novo_adjetivo, traduzir_ingles):

    nova_sentenca = traduzir_ingles.replace(adjetivo, novo_adjetivo[0])
    nova_sentenca_pt = GoogleTranslator(source='english', target='portuguese').translate(nova_sentenca)
    return nova_sentenca_pt


def integra_funcoes(sentenca):

    traduzir_ingles = GoogleTranslator(source='portuguese', target='english').translate(sentenca)
    adjetivo = tokenizacao(traduzir_ingles)
    synonyms, antonyms = sinonimos_antonimos(adjetivo)
    novo_adjetivo = escolhe_adjetivo(synonyms, antonyms)
    nova_sentenca_pt = traduz_sentenca_mod(adjetivo, novo_adjetivo,traduzir_ingles)
    return nova_sentenca_pt

