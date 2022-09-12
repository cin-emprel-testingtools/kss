import math

class Calculadora:

    def raizquadrada(valor):
        """soma = math.sqrt(valor)
        print(f'A raiz quadrada de {valor} é {soma}')"""
        return math.sqrt(valor)

    def soma(self, valor1, valor2):
        return valor1 + valor2

    def subtracao(self,valor1,valor2):
        return valor1 - valor2

    def multiplicacao(self,valor1, valor2):
        return valor1 * valor2

    def divisao(self,valor1, valor2):
        return valor1 / valor2


    print('---------------------------------------------------------')
    print('                    Calculadora                          ')
    print('---------------------------------------------------------')

    '''
    valor1 = int(input('Informe o primeiro valor '))
    valor2 =int(input('Informe o segundo valor '))
    '''

if __name__ == '__main__':
    calc = Calculadora() #instanciando objeto

    #TEST SOMA

    #comportament observado
    result = calc.soma(5,5)

    #comportamento esperado
    esperado = 10

    #test

    if result != esperado:
        print(f'FALHOU! o teste esperava o valor {esperado}, mas retornou {result}')
    else:
        print('PASSOU')



