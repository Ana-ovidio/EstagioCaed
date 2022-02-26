class MudaVoz():

    def __init__(self, objeto, sujeito, tagged, posicao_verbo,
                 posicao_sujeito, posicao_objeto):
        self.objeto = objeto
        self.sujeito = sujeito
        self.tagged = tagged
        self.posicao_verbo = posicao_verbo
        self.posicao_sujeito = posicao_sujeito
        self.posicao_objeto = posicao_objeto

    def modificar_para_ativa(self, verbo_passado):

        novo_texto = []

        # Responsável por realizar as trocas
        for i in range(len(self.tagged)):

            # Modifica verbo principal
            if i == self.posicao_verbo:
                novo_texto.append(verbo_passado)

            # Troca sujeito pelo objeto e vice-versa
            elif i == self.posicao_sujeito:
                novo_texto.append(self.objeto)
            elif i == self.posicao_objeto:
                novo_texto.append(self.sujeito)

            else:
                novo_texto.append(self.tagged[i][0])

        # Remove verbo no participio passado
        novo_texto.pop(self.posicao_verbo + 1)

        # Excluir o by pois essa preposição não existe na voz ativa
        novo_texto.remove('by')

        return novo_texto

    def modificar_para_passiva(self, verbo_participio_passado):

        novo_texo = []
        for tag in self.tagged:
            if tag[0] == self.objeto:
                tag_objeto = tag[1]
        for i in range(len(self.tagged)):

            if i == self.posicao_verbo:

                # Valida qual conjugação do verbo to be no passado se adequa ao objeto
                # O objeto será o novo sujeito
                if ((tag_objeto == 'NNS') or
                        (tag_objeto in ['they', 'They', 'we', 'We', 'you', 'You'])):
                    novo_texo.append('were')
                else:
                    novo_texo.append('was')
                novo_texo.append(verbo_participio_passado)

            elif i == self.posicao_sujeito:
                novo_texo.append(self.objeto)
            elif i == self.posicao_objeto:
                # Adicionar a preposição by
                novo_texo.insert(i, 'by')
                novo_texo.append(self.sujeito)
            else:
                novo_texo.append(self.tagged[i][0])

        return novo_texo
