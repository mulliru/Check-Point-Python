# exemplo que testa o desempenho dos algoritmos....

from algoritmos import busca
import time

class Performance:
    def __init__(self):
        self.lista_ordenada = [i for i in range(1000000)]
        self.lista_ordenada.sort()
        self.lista_desordenada = [i for i in range(1000000)]
        self.lista_desordenada.reverse()

    def test_performance_busca_sequencial(self):
        print("Teste de performance para busca sequencial.")
        inicio = time.time()
        busca.Busca.busca_sequencial(self.lista_ordenada, 999999)
        fim = time.time()
        print(f"Lista ordenada em: {fim - inicio:.2} segundos.")
        inicio = time.time()
        busca.Busca.busca_sequencial(self.lista_desordenada, 999999)
        fim = time.time()
        print(f"Lista desordenada em: {fim - inicio:.2} segundos.\n")

    def test_performance_busca_binaria(self):
        print("Teste de performance para busca binária.")
        inicio = time.time()
        busca.Busca.busca_binaria(self.lista_ordenada, 999999)
        fim = time.time()
        print(f"Lista ordenada em: {fim - inicio:.2} segundos.")
        inicio = time.time()
        busca.Busca.busca_binaria(self.lista_desordenada, 999999)
        fim = time.time()
        print(f"Lista desordenada em: {fim - inicio:.2} segundos.")

    def run_tests(self):
        self.test_performance_busca_sequencial()
        self.test_performance_busca_binaria()
        print("Todos os testes de performance foram executados.")

if __name__ == '__main__':
    testes = Performance()
    testes.run_tests()