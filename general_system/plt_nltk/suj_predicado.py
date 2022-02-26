import nltk
from deep_translator import GoogleTranslator
from class_permuta import Permutacoes


def tokenizacao(traduzir_ingles):
    tokens = nltk.word_tokenize(traduzir_ingles)
    if '.' in tokens:
        tokens.remove('.')
    # Lista de tuplas cujos elementos são respectivamente a palavra e sua morfologia
    tagged = nltk.pos_tag(tokens)
    return tagged


def permutacao_suj_pred(tagged):
    pe = Permutacoes(tagged=tagged)
    sujeito, aposto, predicado = pe.separa_elementos_oracao()
    if aposto is not None:
        permt_suj_apost = pe.permutacao_sujeito_aposto(sujeito, aposto=aposto)
    else:
        permt_suj_apost = pe.permutacao_sujeito_aposto(sujeito)
    permutacoes = pe.permutacao_sujeito_predicado(permt_suj_apost, predicado)
    for i, permutacao in enumerate(permutacoes):
        if permutacao[-1] != '.':
            permutacao = permutacao + '.'
        permutacao = \
            GoogleTranslator(source='english', target='portuguese').translate(permutacao)
        permutacoes[i] = permutacao
    return permutacoes


def integra_funcoes(sentenca):
    traduzir_ingles = \
        GoogleTranslator(source='portuguese', target='english').translate(sentenca)
    tagged = tokenizacao(traduzir_ingles)
    permutacoes = permutacao_suj_pred(tagged)
    return permutacoes


