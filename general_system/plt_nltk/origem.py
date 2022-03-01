import time
import os
import general_system.plt_nltk.troca_genero
import general_system.plt_nltk.troca_adj
import general_system.plt_nltk.sem_sujeito
import general_system.plt_nltk.suj_predicado
import general_system.plt_nltk.modifica_vozes
import general_system.plt_nltk.separacao_silabica
from general_system import app
from general_system.plt_nltk.complexidade import Complexidade


def estima_complexidade(sentenca, lista_modificacoes, opcoes_mudanca):
    cmplx = Complexidade(sentenca, lista_modificacoes, opcoes_mudanca)
    nivel_ensino = cmplx.define_complexidade()
    return nivel_ensino


def create_file_txt(sentenca, lista_modificacoes, opcoes_mudanca,
                    nivel_ensino, nome_arquivo):
    horario = time.strftime("%Y%m%d-%H%M%S")
    all_path = os.path.join(app.root_path, 'static/results', nome_arquivo)
    caminho = 'results/{}'.format(nome_arquivo)
    with open(all_path, 'w') as txt:
        txt.write(f'Sentença informada pelo autor/ pela autora:\n')
        txt.write(f'{sentenca}\n')
        txt.write('----------------------------------------')
        txt.write(f'\n\nMODIFICAÇÕES\n')
        for modificacao in lista_modificacoes:

            if modificacao == opcoes_mudanca[0]:
                nova_sentenca = general_system.plt_nltk.troca_genero.integra_funcoes(sentenca)
                txt.write(f'{opcoes_mudanca[0]}:\n{nova_sentenca}\n')
                txt.write('----------------------------------------')
                txt.write('\n')

            elif modificacao == opcoes_mudanca[1]:
                nova_sentenca = general_system.plt_nltk.troca_adj.integra_funcoes(sentenca)
                txt.write(f'{opcoes_mudanca[1]}:\n{nova_sentenca}\n')
                txt.write('----------------------------------------')
                txt.write('\n')

            elif modificacao == opcoes_mudanca[2]:
                permutacoes = general_system.plt_nltk.sem_sujeito.integra_funcoes(sentenca)
                txt.write(f'Permutações entre orações sem sujeito:\n')
                for permutacao in permutacoes:
                    txt.write(f'{permutacao}\n')
                txt.write('----------------------------------------')
                txt.write('\n')

            elif modificacao == opcoes_mudanca[3]:
                permutacoes = general_system.plt_nltk.suj_predicado.integra_funcoes(sentenca)
                txt.write(f'Permutações entre elementos de uma oração:\n')
                for permutacao in permutacoes:
                    txt.write(f'{permutacao}\n')
                txt.write('----------------------------------------')
                txt.write('\n')

            elif modificacao == opcoes_mudanca[4]:
                nova_sentenca = general_system.plt_nltk.modifica_vozes.integra_funcoes(sentenca)
                txt.write(f'Modificação de voz ativa e passiva:\n{nova_sentenca}\n')
                txt.write('----------------------------------------')
                txt.write('\n')
            else:
                palavras_canonicas = general_system.plt_nltk.separacao_silabica.integra_funcoes(sentenca)
                txt.write(f'{opcoes_mudanca[5]}:\n')
                for palavra in palavras_canonicas:
                    txt.write(f'{palavra}\n')
                txt.write('----------------------------------------')
                txt.write('\n')
        txt.write(f'\nNÍVEL DE COMPLEXIDADE: {nivel_ensino}\n')
    txt.close()
    return caminho


def modifica_body_text(lista_modificacoes, sentenca, nome_arquivo):
    opcoes_mudanca = ['Trocar de gênero',
                      'Trocar adjetivos por sinônimo/antônimos',
                      'Paráfrase i',
                      'Paráfrase ii',
                      'Paráfrase iii',
                      'Palavras canônicas']

    nome_arquivo = nome_arquivo+'.txt'
    nivel_ensino = estima_complexidade(sentenca,
                                       lista_modificacoes,
                                       opcoes_mudanca)
    caminho = create_file_txt(sentenca, lista_modificacoes, opcoes_mudanca,
                              nivel_ensino, nome_arquivo)
    return caminho
