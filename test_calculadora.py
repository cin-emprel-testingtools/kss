import pytest
from calculadora import Calculadora


class TestCalculadora(): #suite de testes

    def setup_class(self): #execcutado uma UNICA vez para a classe toda
        self.calc = Calculadora() #instanciando objeto

    def teardown_class(self): #executado uma unica vez  para a classe toda
        pass

    def setup_method(self): #metodo que é chamado antes de cada CASO de teste ser executado
        self.calc = Calculadora() #instanciando objeto
        #print('\n********Rodou')

    def teardown_method(self): #Metodo chamado apos cada CASO
      #  print('\nFIM DO CASO')
      pass

    @pytest.mark.skip(reason="pq Deus quis")
    def test_soma(self): #caso de teste
        assert self.calc.soma(3,5) == 8 #oraculo

    def test_subtracao(self):
        assert self.calc.subtracao(3,2) == 1

    def test_divisao(self):
        assert self.calc.divisao(10,5) ==2

    def test_multiplicacao(self):
        assert self.calc.multiplicacao(4,2)==8

    #error

    def test_error_soma(self):
        assert self.calc.soma(2,5)==7

    #exeption

    def test_divisaoPZero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.divisao(10,0)
