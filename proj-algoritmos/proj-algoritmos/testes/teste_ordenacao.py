import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from algoritmos.ordenacao import Ordenacao

class TesteOrdenacao:
    def __init__(self) -> None:
        self.dicionario_de_listas = {
        "lista ordenada crescente": [3, 7, 33, 59, 71],
        "lista não ordenada": [71, 7, 3, 9, 7],
        "lista ordenada decrescente": [71, 59, 33, 7, 3],
        "lista vazia": [],
        "lista de elemento único": [42],
        "lista de elementos repetidos": [3, 7, 3, 9, 7]
    }

    def test_bubble_sort(self):
        for nome_lista, lista in self.dicionario_de_listas.items():
            Ordenacao.bubble_sort(lista)
            print(f"Lista ordenada para {nome_lista}: {lista}")

    def test_selection_sort(self):
        for nome_lista, lista in self.dicionario_de_listas.items():
            lista_copy = lista[:]
            Ordenacao.selection_sort(lista_copy)
            print(f"Lista ordenada para {nome_lista}: {lista_copy}")

    def test_insertion_sort(self):
        for nome_lista, lista in self.dicionario_de_listas.items():
            lista_copy = lista[:]
            Ordenacao.insertion_sort(lista_copy)
            print(f"Lista ordenada para {nome_lista}: {lista_copy}")

    def test_merge_sort(self):
        for nome_lista, lista in self.dicionario_de_listas.items():
            lista_copy = lista[:]
            Ordenacao.merge_sort(lista_copy)
            print(f"Lista ordenada para {nome_lista}: {lista_copy}")

    def test_quick_sort(self):
        for nome_lista, lista in self.dicionario_de_listas.items():
            lista_copy = lista[:]
            Ordenacao.quick_sort(lista_copy)
            print(f"Lista ordenada para {nome_lista}: {lista_copy}")

    def run_tests(self):
        print("\nTeste Bubble Sort:\n")
        self.test_bubble_sort()
        print("\nTeste Selection Sort:\n")
        self.test_selection_sort()
        print("\nTeste Insertion Sort:\n")
        self.test_insertion_sort()
        print("\nTeste Merge Sort:\n")
        self.test_merge_sort()
        print("\nTeste Quick Sort\n")
        self.test_quick_sort()
        print("\nFim dos testes de ordenação.\n")

if __name__ == '__main__':
    testes = TesteOrdenacao()
    testes.run_tests()
