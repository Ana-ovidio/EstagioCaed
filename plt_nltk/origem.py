import time
import troca_genero
import troca_adj
import sem_sujeito
import suj_predicado
import modifica_vozes
import separacao_silabica
from complexidade import Complexidade


def estima_complexidade(sentenca, lista_modificacoes, opcoes_mudanca):
    cmplx = Complexidade(sentenca, lista_modificacoes, opcoes_mudanca)
    nivel_ensino = cmplx.define_complexidade()
    return nivel_ensino


def create_file_txt(sentenca, lista_modificacoes, opcoes_mudanca,
                    nivel_ensino, nome_arquivo):
    horario = time.strftime("%Y%m%d-%H%M%S")
    caminho = '../../results/'
    with open(caminho + f'{nome_arquivo}.txt', 'w') as txt:
        txt.write(f'Sentença informada pelo autor/ pela autora:\n')
        txt.write(f'{sentenca}\n')
        txt.write('----------------------------------------')
        txt.write(f'\n\nMODIFICAÇÕES\n')
        for modificacao in lista_modificacoes:

            if modificacao == opcoes_mudanca[0]:
                nova_sentenca = troca_genero.integra_funcoes(sentenca)
                txt.write(f'{opcoes_mudanca[0]}:\n{nova_sentenca}\n')
                txt.write('----------------------------------------')
                txt.write('\n')

            elif modificacao == opcoes_mudanca[1]:
                nova_sentenca = troca_adj.integra_funcoes(sentenca)
                txt.write(f'{opcoes_mudanca[1]}:\n{nova_sentenca}\n')
                txt.write('----------------------------------------')
                txt.write('\n')

            elif modificacao == opcoes_mudanca[2]:
                permutacoes = sem_sujeito.integra_funcoes(sentenca)
                txt.write(f'Permutações entre orações sem sujeito:\n')
                for permutacao in permutacoes:
                    txt.write(f'{permutacao}\n')
                txt.write('----------------------------------------')
                txt.write('\n')

            elif modificacao == opcoes_mudanca[3]:
                permutacoes = suj_predicado.integra_funcoes(sentenca)
                txt.write(f'Permutações entre elementos de uma oração:\n')
                for permutacao in permutacoes:
                    txt.write(f'{permutacao}\n')
                txt.write('----------------------------------------')
                txt.write('\n')

            elif modificacao == opcoes_mudanca[4]:
                nova_sentenca = modifica_vozes.integra_funcoes(sentenca)
                txt.write(f'Modificação de voz ativa e passiva:\n{nova_sentenca}\n')
                txt.write('----------------------------------------')
                txt.write('\n')
            else:
                palavras_canonicas = separacao_silabica.integra_funcoes(sentenca)
                txt.write(f'{opcoes_mudanca[5]}:\n')
                for palavra in palavras_canonicas:
                    txt.write(f'{palavra}\n')
                txt.write('----------------------------------------')
                txt.write('\n')
        txt.write(f'\nNÍVEL DE COMPLEXIDADE: {nivel_ensino}\n')
    txt.close()


def modifica_bory_text(lista_modificacoes, sentenca, nome_arquivo):
    opcoes_mudanca = ['Trocar de gênero',
                      'Trocar adjetivos por sinônimo/antônimos',
                      'Paráfrase i',
                      'Paráfrase ii',
                      'Paráfrase iii',
                      'Palavras canônicas']

    nivel_ensino = estima_complexidade(sentenca,
                                       lista_modificacoes,
                                       opcoes_mudanca)
    create_file_txt(sentenca, lista_modificacoes, opcoes_mudanca,
                    nivel_ensino, nome_arquivo)
