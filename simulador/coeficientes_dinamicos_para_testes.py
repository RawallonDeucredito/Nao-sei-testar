from simulacao.simulacao_financeira import SimulacaoFinanceira
import simulacao


class CoeficientesDinamicosParaTestes():

    coefs = {}
    
    def __init__(self):
        print('init', type(simulacao.simulacao_financeira.SimulacaoFinanceira))

    def get_coeficientes(self):
        sf = simulacao.simulacao_financeira.SimulacaoFinanceira()
        print('get_coeficientes', type(sf))
