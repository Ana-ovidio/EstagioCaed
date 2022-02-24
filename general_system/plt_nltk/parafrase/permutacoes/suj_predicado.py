import nltk
from deep_translator import GoogleTranslator
from class_permutacao import Permutacoes

sentenca = 'O cantor Roberto Carlos fez aniversário'
traduzir_ingles  =\
    GoogleTranslator(source='portuguese', target='english').translate(sentenca)

tokens = nltk.word_tokenize(traduzir_ingles)
#Lista de tuplas cujos elementos são respectivamente a palavra e sua morfologia
tagged = nltk.pos_tag(tokens) 

pe = Permutacoes(tagged=tagged)
sujeito, aposto, predicado = pe.separa_elementos_oracao()

if aposto != None:
    permt_suj_apost = pe.permutacao_sujeito_aposto(sujeito, aposto=aposto)
    
else:
    permt_suj_apost = pe.permutacao_sujeito_aposto(sujeito)

permutacoes = pe.permutacao_sujeito_predicado(permt_suj_apost, predicado)

for i, permutacao in enumerate(permutacoes):
    if permutacao[-1]!= '.':
        permutacao = permutacao + '.'
    permutacao =\
        GoogleTranslator(source='english', target='portuguese').translate(permutacao) 
    permutacoes[i] = permutacao

print(permutacoes)