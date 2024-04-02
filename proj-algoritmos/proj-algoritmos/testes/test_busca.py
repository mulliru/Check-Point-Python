import sys
import os

# Adiciona o diretório pai ao sys.path para que seja possível importar o módulo que será testado
# (nesse caso, o módulo busca.py)
# referencia para o código abaixo: https://diveintopython.org/learn/file-handling/directories 
# O `sys.path` é uma lista de diretórios onde o Python procura por módulos
# O `os.path.abspath` retorna o caminho absoluto do arquivo que está sendo executado
# O `os.path.dirname` retorna o diretório onde o arquivo que está sendo executado está localizado
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../") # resolve o problema de import do módulo busca.py

from algoritmos.busca import Busca

import random

class TestBusca:
    def __init__(self):
        self.lista_ordenada = [3, 5, 7, 9, 27, 34, 63, 88, 89]

    # Forma simples de fazer um teste de unidade para a busca sequencial    
    def test_busca_sequencial(self):
        valor = [random.randint(1, 100) for _ in range(5)]
        
        for v in valor:
            try:
                if Busca.busca_sequencial(self.lista_ordenada, v) == self.lista_ordenada.index(v):
                    print(f"Teste de busca sequencial ({v}) passou.")
            except:
                print(f"Teste de busca sequencial ({v}) falhou.")              


    # O `assert` é uma forma de testar se a condição é verdadeira ou falsa e caso seja falsa,
    # o programa para de rodar e mostra o erro que ocorreu na linha do assert que falhou 
    # https://pt.stackoverflow.com/questions/85323/pra-que-serve-o-assert-no-python
    def test_busca_binaria(self):
        try:
            assert Busca.busca_binaria(self.lista_ordenada, 34) == 5
            assert Busca.busca_binaria(self.lista_ordenada, 88) == 7
            assert Busca.busca_binaria(self.lista_ordenada, 50) == 4
            print("Teste de busca binária passou.")
        except AssertionError:
            print("Teste de busca binária falhou.")
            return
 

    # O método `run_tests` chama todos os testes que foram implementados
    def run_tests(self):
        self.test_busca_sequencial()
        self.test_busca_binaria()
        print("Fim dos testes.")

if __name__ == '__main__':
    testes = TestBusca()
    testes.run_tests()
