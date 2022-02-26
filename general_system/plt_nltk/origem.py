import troca_genero
import troca_adj
import sem_sujeito
import suj_predicado
import modifica_vozes
import separacao_silabica

lista_modificacoes = ['Paráfrase iii']
sentenca = 'A mulher pegou o objeto'

opcoes_mudanca = ['Trocar de gênero',
                  'Trocar adjetivos por sinônimo/antônimos',
                  'Paráfrase i',
                  'Paráfrase ii',
                  'Paráfrase iii',
                  'Palavras canônicas']

for modificacao in lista_modificacoes:

    if modificacao == opcoes_mudanca[0]:
        nova_sentenca = troca_genero.integra_funcoes(sentenca)
        print(nova_sentenca)

    elif modificacao == opcoes_mudanca[1]:
        nova_sentenca = troca_adj.integra_funcoes(sentenca)
        print(nova_sentenca)

    elif modificacao == opcoes_mudanca[2]:
        permutacoes = sem_sujeito.integra_funcoes(sentenca)
        print(permutacoes)

    elif modificacao == opcoes_mudanca[3]:
        permutacoes = suj_predicado.integra_funcoes(sentenca)
        print(permutacoes)

    elif modificacao == opcoes_mudanca[4]:
        nova_sentenca = modifica_vozes.integra_funcoes(sentenca)
        print(nova_sentenca)

    else:
        palavras_canonicas = separacao_silabica.integra_funcoes(sentenca)
        print(palavras_canonicas)