from simulacao.simulacao_financeira import SimulacaoFinanceira


class CoeficientesDinamicos():

    coefs = {}
    
    def __init__(self):
        print('init', type(SimulacaoFinanceira()))

    def get_coeficientes(self):
        sf = SimulacaoFinanceira()
        print('get_coeficientes', sf.__dict__, type(sf))
