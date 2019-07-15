class Nome:
    '''
        Pensado para fazer analises com nomes
    '''
    def __init__(self, name:str):
        # armazena a base
        if len( name ) > 0:
            self.base = name
            #armazena a informacao do priemiro nome
            self.listPrimeirasLetras = list()
            self.listNome = list()
            self.listNomeGrandes = list()
            self.__casamento = list()

            self.inicio()



    def inicio(self):
        #cortar o nome em partes pelo " "
        apo = self.base.lower()
        if " " in apo:
            self.listNome = apo.split(' ')
        else:
            self.listNome = [apo]

        for ele in self.listNome:
            if len( ele ) > 1:
                self.listNomeGrandes.append( ele )

        for ele in self.listNome:
            self.listPrimeirasLetras.append( ele[ 0 ])
        