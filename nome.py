vogais = {"a", "e", "o", "i", "u"}
class Nome:
    '''
        Pensado para fazer analises com nomes
    '''
    def __init__(self, name:str):
        # armazena a base
        name = name.replace(".", "")
        self.base = name
        #armazena a informacao do priemiro nome
        self.listPrimeirasLetras = list()
        self.listNome = list()
        self.listNomeGrandes = list()
        self.__casamento = list()
        if len( name ) > 0:
            self.inicio()

    def __str__(self):
        return f"[{self.base}]"

    def inicio(self):
        #cortar o nome em partes pelo " "
        apo = self.base.lower()
        apo = apo.replace("  ", "")
        apo = apo.strip(" ")
        if " " in apo:
            self.listNome = apo.split(' ')
        else:
            self.listNome = [apo]

        for ele in self.listNome:
            if len( ele ) > 1:
                self.listNomeGrandes.append( ele )
            elif len( ele ) == 2:
                if vogais not in ele:
                    self.listNomeGrandes.append( ele[ 0 ])
                    self.listNomeGrandes.append( ele[ 1 ])


        for ele in self.listNome:
            self.listPrimeirasLetras.append( ele[ 0 ])
        