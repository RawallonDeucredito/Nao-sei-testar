from unittest.mock import patch
from django.test import TestCase
from simulador.coeficientes_dinamicos_para_testes import CoeficientesDinamicosParaTestes
from simulador.coeficientes_dinamicos import CoeficientesDinamicos
from simulacao.simulacao_financeira import SimulacaoFinanceira

import simulacao
import simulador

class TestCoeficientesDinamicos(TestCase):

    @patch("simulacao.simulacao_financeira.SimulacaoFinanceira")
    def test_mock_working(self, mock_sf):
        # Esse passa!
        simulacao.simulacao_financeira.SimulacaoFinanceira()
        assert mock_sf is simulacao.simulacao_financeira.SimulacaoFinanceira
        assert mock_sf.called

    @patch("simulacao.simulacao_financeira.SimulacaoFinanceira")
    def test_not_mock_working(self, mock_sf):
        # Esse NÃO passa!
        SimulacaoFinanceira()
        assert mock_sf is SimulacaoFinanceira
        assert mock_sf.called

    @patch("simulacao.simulacao_financeira.SimulacaoFinanceira")
    def test_coeficiente_dinamico(self, mock_sf):
        # Esse NÃO passa!
        self.assertEquals(mock_sf,simulacao.simulacao_financeira.SimulacaoFinanceira)
        # simulador.coeficientes_dinamicos.CoeficientesDinamicos() # wtf
        CoeficientesDinamicos().get_coeficientes()
        assert mock_sf.called

    @patch("simulacao.simulacao_financeira.SimulacaoFinanceira")
    def test_coeficiente_dinamico_que_passa(self, mock_sf):
        # Esse passa!
        self.assertEquals(mock_sf,simulacao.simulacao_financeira.SimulacaoFinanceira)
        CoeficientesDinamicosParaTestes().get_coeficientes()
        assert mock_sf.called


    @patch("simulacao.simulacao_financeira.SimulacaoFinanceira", new_callable=SimulacaoFinanceira)
    def test_coeficiente_dinamico(self, mock_sf):
        # Esse Não passa!
        self.assertEquals(mock_sf,simulacao.simulacao_financeira.SimulacaoFinanceira)
        mock_sf.return_value = "return_value"
        CoeficientesDinamicos().get_coeficientes()
        assert SimulacaoFinanceira.called