import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from algoritmos.ordenacao import Ordenacao

class TesteOrdenacao:
    def __init__(self) -> None:
        self.conjunto_listas = {
        "lista ordenada crescente": [3, 7, 33, 59, 71],
        "lista não ordenada": [71, 7, 3, 9, 7],
        "lista ordenada decrescente": [71, 59, 33, 7, 3],
        "lista vazia": [],
        "lista de elemento único": [42],
        "lista de elementos repetidos": [3, 7, 3, 9, 7]
    }
    #teste do bubble sort
    def test_bs(self):
        for nome_lista, lista in self.conjunto_listas.items():
            Ordenacao.bubble_sort(lista)
            print(f"O resultado para a lista é:\n {nome_lista}: {lista}")
            
    #teste do selection sort
    def test_ss(self):
        for nome_lista, lista in self.conjunto_listas.items():
            lista_copy = lista[:]
            Ordenacao.selection_sort(lista_copy)
            print(f"O resultado para a lista é:\n {nome_lista}: {lista_copy}")
            
    #teste do insertion sort
    def test_is(self):
        for nome_lista, lista in self.conjunto_listas.items():
            lista_copy = lista[:]
            Ordenacao.insertion_sort(lista_copy)
            print(f"O resultado para a lista é:\n {nome_lista}: {lista_copy}")
    #teste do merge sort
    def test_ms(self):
        for nome_lista, lista in self.conjunto_listas.items():
            lista_copy = lista[:]
            Ordenacao.merge_sort(lista_copy)
            print(f"O resultado para a lista é:\n {nome_lista}: {lista_copy}")
            
    #teste do quick sort
    def test_qs(self):
        for nome_lista, lista in self.conjunto_listas.items():
            lista_copy = lista[:]
            Ordenacao.quick_sort(lista_copy)
            print(f"O resultado para a lista é:\n {nome_lista}: {lista_copy}")

    def run_tests(self):
        print("\nTeste Bubble Sort:\n")
        self.test_bs()
        print("\nTeste Selection Sort:\n")
        self.test_ss()
        print("\nTeste Insertion Sort:\n")
        self.test_is()
        print("\nTeste Merge Sort:\n")
        self.test_ms()
        print("\nTeste Quick Sort\n")
        self.test_qs()
        print("\nFim dos testes de ordenação.\n")

if __name__ == '__main__':
    testes = TesteOrdenacao()
    testes.run_tests()
