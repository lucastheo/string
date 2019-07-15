from casamento import CasamentoNome
from nome import Nome


if __name__ == "__main__":
    listaNomes = list()
    listaNomes.append("Lucas Theodoro")
    listaNomes.append("Lucas T")
    listaNomes.append("Theodoro L")
    listaNomes.append("Guimaraes de Almeida L T")
    listaNomes.append("Luca Theodoro")
    listaNomes.append("Lucas Thiodoro")
    listaNomes.append("L T")
    listaNomes.append("Lucas")

    objCasa = CasamentoNome()

    for ele in listaNomes:
        apoNome = Nome( ele )
        objCasa.julgandoAdicioando( apoNome )
    #objCasa.julgando()
