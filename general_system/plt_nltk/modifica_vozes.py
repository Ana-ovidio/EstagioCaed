import nltk
import pyinflect
import spacy
from deep_translator import GoogleTranslator
from class_mod_vozes import MudaVoz

spacy.cli.download("en_core_web_sm")


def verifica_virgula(traduzir_ingles):
    palavra_antes_verbo = None
    entre_virgulas = None

    tokens = nltk.word_tokenize(traduzir_ingles)
    tagged = nltk.pos_tag(tokens)

    for i, tag in enumerate(tagged):
        if tag[0] == ',':
            palavra_antes_verbo = tagged[i - 1][0]
            break

    # Armazenar em uma string o trecho entre vírgula
    # Retirar esse trecho da sentenca em inglês por enquanto
    if palavra_antes_verbo is not None:
        for i in range(len(traduzir_ingles)):
            if traduzir_ingles[i] == ',':
                posicao_virgula1 = i
                break

        for i in range(posicao_virgula1 + 1, len(traduzir_ingles)):
            if traduzir_ingles[i] == ',':
                posicao_virgula2 = i
                break

        entre_virgulas = traduzir_ingles[posicao_virgula1:posicao_virgula2 + 1]
        traduzir_ingles = traduzir_ingles.replace(entre_virgulas, "")

    return traduzir_ingles, palavra_antes_verbo, entre_virgulas


def tokenizacao(traduzir_ingles):
    tokens = nltk.word_tokenize(traduzir_ingles)
    # Lista de tuplas cujos elementos são respectivamente a palavra e sua morfologia
    tagged = nltk.pos_tag(tokens)

    return tagged


def inverter_voz(traduzir_ingles, tagged, posicao_verbo, posicao_sujeito, posicao_objeto,
                 objeto, sujeito):
    nlp = spacy.load("en_core_web_sm")
    doc_dep = nlp(traduzir_ingles)

    mv = MudaVoz(objeto, sujeito, tagged, posicao_verbo, posicao_sujeito,
                 posicao_objeto)

    verbo_passado = None
    verbo_participio_passado = None

    # Verifica se a voz é passiva (verb to be in the pass + verb in the past participle)
    if (tagged[posicao_verbo][1] == 'VBD') and (tagged[posicao_verbo + 1][1] == 'VBN'):
        for i in range(1, len(doc_dep)):
            token = doc_dep[i - 1]
            proximo_token = doc_dep[i]
            if (token.tag_ == 'VBD') and (proximo_token.tag_ == 'VBN'):
                verbo_passado = proximo_token._.inflect("VBD")

        # Representa uma lista com a sentenca ordenada para outra voz
        traducao_para_portugues = mv.modificar_para_ativa(
            verbo_passado)


    # Senão a voz é ativa (verb in the past)
    else:
        for i in range(len(doc_dep)):
            token = doc_dep[i]
            if token.tag_ == 'VBD':
                verbo_participio_passado = token._.inflect("VBN")

        # Representa uma lista com a sentenca ordenada para outra voz
        traducao_para_portugues = mv.modificar_para_passiva(
            verbo_participio_passado)
    return traducao_para_portugues


def verifica_voz(tagged, traduzir_ingles):
    # Encontra o objeto da frase
    for i in range(len(tagged) - 1, -1, -1):
        if (tagged[i][1] == 'NN') or (tagged[i][1] == 'NNS'):
            objeto = tagged[i][0]
            posicao_objeto = i
            break

    # Encontra o sujeito da frase
    for i, tag in enumerate(tagged):
        if (tag[1] == 'NN') or (tag[1] == 'NNS'):
            sujeito = tag[0]
            posicao_sujeito = i
            break

    # Encontra a posição do verbo
    for i in range(len(tagged)):
        # Verifica se o token é um verbo (independente do tempo)
        if tagged[i][1][0] == 'V':
            posicao_verbo = i
            break

    traducao_para_portugues = inverter_voz(traduzir_ingles, tagged,
                                           posicao_verbo, posicao_sujeito,
                                           posicao_objeto, objeto, sujeito)
    return traducao_para_portugues


def retifica_string(palavra_antes_verbo, traducao_para_portugues,
                    entre_virgulas):
    if palavra_antes_verbo != None:
        # Uma lista com todos os elementos da string
        entre_virgulas = entre_virgulas.split()

        indice_palavra_antes = traducao_para_portugues.index(palavra_antes_verbo)

        for i in range(len(entre_virgulas)):
            traducao_para_portugues.insert(indice_palavra_antes + 1 + i, entre_virgulas[i])

        # Retirar a segunda vírgula caso entre_virgulas estiver no final da frase na modificação.

        if entre_virgulas[-1] == traducao_para_portugues[-1]:
            ultimo_elemento = entre_virgulas[-1]
            ultimo_elemento = ultimo_elemento.replace(',', "")
            traducao_para_portugues[-1] = ultimo_elemento
        else:
            pass

        traducao_para_portugues = " ".join(traducao_para_portugues)

    else:
        traducao_para_portugues = " ".join(traducao_para_portugues)

    return traducao_para_portugues


def retorno_portugues(traducao_para_portugues):
    traducao_para_portugues = traducao_para_portugues + '.'
    nova_sentenca = \
        GoogleTranslator(source='english', target='portuguese').translate(traducao_para_portugues)
    return nova_sentenca


def integra_funcoes(sentenca):
    if '.' in sentenca:
        sentenca = sentenca.replace('.', '')

    traduzir_ingles = \
        GoogleTranslator(source='portuguese', target='english').translate(sentenca)

    traduzir_ingles, palavra_antes_verbo, entre_virgulas = \
        verifica_virgula(traduzir_ingles)

    tagged = tokenizacao(traduzir_ingles)
    traducao_para_portugues = verifica_voz(tagged, traduzir_ingles)
    traducao_para_portugues = retifica_string(palavra_antes_verbo,
                                              traducao_para_portugues,
                                              entre_virgulas)
    nova_sentenca = retorno_portugues(traducao_para_portugues)

    return nova_sentenca
