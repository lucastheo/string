
import Levenshtein

def distanciaString( nome0:str, nome1:str):
    return Levenshtein.distance( nome0 , nome1 )
def distanciaNome( nome0 , nome1 ):
    flagNomeReduzido = False
    valor = 0
    if len( nome0.listNome ) > 1 and len( nome0.listNome ) > 1:
        for apo0 in nome0.listNomeGrandes:
            for apo1 in nome1.listNomeGrandes:
                if distanciaString( apo0 , apo1 ) < 1:
                    valor = casouUmNome( nome0, nome1, apo0, apo1 )
    else:
        if existeNomeIgual( nome0.listNome, nome0.listNome ) == True:
            valor = 0.3
    return valor

def casouUmNome(nome0, nome1, apo0, apo1):
    '''
    verica se existe uma forma de casamento
    '''

    listApo0 = nome0.listNome[:]
    listApo1 = nome1.listNome[:]

    listApo0.remove(apo0)
    listApo1.remove(apo1)

    # primeiro teste tem nome grande igual
    if existeNomeIgual( listApo0, listApo1 ) == True:
        return 1
    quant = quantidadePrimeiraLetraIgual( listApo0, listApo1 )
    if quant > 0:
        if quant == 1:
            return 0.6
        else:
            return 0.8

    return 0.2
def existeNomeIgual(lista0:list, lista1:list):
    '''
    Percore todos os nome e verifica se existe um grande com distancia menor que 2
    '''
    for nome0 in lista0:
        if len( nome0 ) > 1:
            for nome1 in lista1:
                if len( nome1) > 1:
                    calc = distanciaString( nome0 , nome1 )
                    if calc < 2 :
                        return True
    return False
def quantidadePrimeiraLetraIgual( lista0:list, lista1:list):
    '''
    Percorre os nomes verificando se tem nome parecido
    '''
    cont = 0
    apoList1 = lista1[:]
    for nome0 in lista0:
        apo0 = nome0[0]
        for nome1 in apoList1:
            apo1 = nome1[0]
            if apo0 == apo1:
                cont += 1    
                apoList1.remove( nome1)
                break
    return cont




class CasamentoNome:
    def __init__(self):
        # é uma lista com nomes
        self.nomes = list()
        self.hashCasamento = dict()
        self.grupos = list()

    def add( self, nome ):
        self.nomes.append( nome )

    def julgandoAdicioando( self, nome ):
        nomeBase = nome.base
        if nomeBase in self.hashCasamento:
            index = self.hashCasamento[ nome ]
            return self.grupos[ index ]
        
        maximo = -1
        valorMaximo = 0
        valor = 0

        for i in range( len( self.grupos ) ):
            grupo = self.grupos[ i ]
            
            valor = 0
            for apoNome in grupo:
                valor += distanciaNome( nome, apoNome )            
            valor = valor / len( grupo )

            if valor > valorMaximo:
                valorMaximo = valor
                maximo = i
        if valorMaximo < 0.2:
            maximo =  len( self.grupos )
            self.hashCasamento[ nomeBase ] = maximo
            self.grupos.append( [nome ] )
        else:
            grupo.append( nome )
        print( maximo )    
        return maximo