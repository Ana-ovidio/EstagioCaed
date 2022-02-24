from itertools import permutations


class Permutacoes ():
    
    def __init__(self, tagged=None, oracoes=None):
        self.tagged = tagged
        self.oracoes = oracoes
        
    def separa_elementos_oracao (self):
    
        sujeito = []
        predicado = []
    
        #Separar o sujeito do predicado
        for i,tag in enumerate(self.tagged):
            if tag[1][0]== 'V':
                break
            else:
                sujeito.append(tag)
                
        for j in range(i,len(self.tagged)):
            predicado.append(self.tagged[j][0])
        predicado_concatenado = []
        predicado_concatenado.append(' '.join(predicado))
           
        #Separar o sujeito principal do aposto se exixtir
        aposto = []
        sujeito_principal = []
    
        for i in range(1,len(sujeito)):
            
            if (sujeito[i][1] == 'NNP') and (sujeito[i-1][1] in ['NN', 'NNS']):
                sujeito_principal.append(sujeito[i][0])
                aposto.append(sujeito[i-1][0])
            elif (sujeito[i][1] == 'NNP') and (sujeito[i-1][1] == 'NNP'):
                sujeito_principal.append(sujeito[i][0])
            else:
                aposto.append(sujeito[i-1][0])
                
        suj = [] #sujeito em string
        aposto_suj = [] #aposto em string
    
        suj.append(' '.join(sujeito_principal))
        if len(aposto) != 0:
            aposto_suj.append(' '.join(aposto))
        else:
            aposto_suj.append(None)
            
        return suj[0], aposto_suj[0], predicado_concatenado
    
    def permutacao_sujeito_aposto(self,suj, aposto=None):
    
        if aposto != None:
            primeira_permutacao = list(permutations([suj, aposto]))
        
            #Tranformar tuplas em lista para permitir modificação
            permutacoes = []
            for tupla in primeira_permutacao:
                permutacoes.append(list(tupla))
    
            # Inserir vírgula para inversão da ordem canônica
            for i, permutacao in enumerate(permutacoes):
                if permutacao[0] == aposto:
                    pass
                else:
                    permutacao[1] = permutacao[1].lower()
                    permutacao.insert(1,',')
                    permutacao.insert(3,',')
            # Concatenar strings permutadas
            permutacoes_concatenadas = []
            for i in range(len(permutacoes)):
                permutacoes_concatenadas.append(' '.join(permutacoes[i]))
        
        else:
            permutacoes_concatenadas = [suj]
             
        return permutacoes_concatenadas
    
    def permutacao_sujeito_predicado(self,sujeitos, predicado):
        
        primeira_permutacao = []
        for sujeito in sujeitos:
            primeira_permutacao.append(list(permutations([sujeito, predicado[0]])))
    
        #Tranformar tuplas em lista para permitir modificação
        permutacoes = []
        for lista in primeira_permutacao:
            for tupla in lista:
                permutacoes.append(list(tupla))
                
        #Incluir vírgula caso o predicado venha antes
        for i, permutacao in enumerate(permutacoes):
            
            if permutacao[0] == predicado[0]:
                #Mudar apenas a letra inicial 
                lista_strings = list(permutacao[0])
                lista_strings[0] = lista_strings[0].upper()
                permutacao[0] = ''.join(lista_strings)
                permutacao.insert(1,',')
            else:
                pass
            
            # Concatenar strings permutadas
            permutacoes_concatenadas = []
            for i in range(len(permutacoes)):
        
                if permutacoes[i][-1][-1] == ',':
                    frase_com_virgula = list(permutacoes[i][-1])
                    frase_com_virgula[-1] = '.'
                    permutacoes[i][-1] = ''.join(frase_com_virgula)
                permutacoes_concatenadas.append(' '.join(permutacoes[i]))
    
        return permutacoes_concatenadas

    def permutacao_oracoes (self):
        
        primeira_permutacao = list(permutations(self.oracoes))
        
        #Tranformar tuplas em lista para permitir modificação
        permutacoes = []
        for tupla in primeira_permutacao:
            permutacoes.append(list(tupla))   
        permutacoes_concatenadas = []
        
        #Concatenar as strings
        for permutacao in permutacoes:
            if permutacao[0][0] == permutacao[0][0].upper():
                pass
            else:
                primeira_string = list(permutacao[0])
                primeira_string[0] = primeira_string[0].upper()
                permutacao[0] = ''.join(primeira_string)
                
                segunda_string = list(permutacao[1])
                segunda_string[0] = segunda_string[0].lower()
                permutacao[1] = ''.join(segunda_string)
                
            permutacoes_concatenadas.append(' '.join(permutacao))
        
        return permutacoes_concatenadas