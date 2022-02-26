import nltk
from plt_nltk.class_troca_genero import TrocaGenero


def tratamento_sentenca(sentenca):
    lista_sentenca = list(sentenca)
    lista_sentenca[0] = lista_sentenca[0].upper()
    sentenca = ''.join(lista_sentenca)
    return sentenca


def tokenizacao (sentenca):
    tokens = nltk.word_tokenize(sentenca)
    if '.' in tokens:
        tokens.remove('.')
    return tokens


def define_genero(tokens):
    pronomes_artigos_femininos = ['A','Uma','Alguma','Aquela','Umas','Algumas','Aquelas']
    pronomes_artigos_masculinos = ['O', 'Um', 'Algum', 'Aquele', 'Uns', 'Alguns', 'Aqueles']

    if tokens[0] in pronomes_artigos_femininos:
        genero = 'feminino'
    elif tokens[0] in pronomes_artigos_masculinos:
        genero = 'masculino'
    else:
        genero = None

    return genero


def modifica_genero(genero, tokens):
    tg = TrocaGenero(genero, tokens)

    if tokens[0][-1] != 's':
        numeracao = 'singular'
    else:
        numeracao = 'plural'

    if numeracao == 'singular':
        nova_sentenca = tg.modifica_elementos_sing()
    else:
        nova_sentenca = tg.modifica_elementos_plural()
    nova_sentenca = nova_sentenca + '.'

    return nova_sentenca


def integra_funcoes (sentenca):
    sentenca = tratamento_sentenca(sentenca)
    tokens = tokenizacao(sentenca)
    genero = define_genero(tokens)
    nova_sentenca = modifica_genero(genero, tokens)
    return nova_sentenca


