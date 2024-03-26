# Exemplo de implementação dos algoritmos de busca sequencial e binária.

class Busca:

    def busca_sequencial(lista, alvo):
        """
        Implementação do algoritmo de busca sequencial.

        :param lista: Lista onde será realizada a busca.
        :param alvo: Elemento a ser buscado.
        :return: Índice do elemento alvo se encontrado, caso contrário -1.
        """
        for indice, elemento in enumerate(lista):
            if elemento == alvo:
                return indice
        return -1

    def busca_binaria(lista, alvo):
        """
        Implementação do algoritmo de busca binária.
        Assume que a lista está ordenada.

        :param lista: Lista ordenada onde será realizada a busca.
        :param alvo: Elemento a ser buscado.
        :return: Índice do elemento alvo se encontrado, caso contrário -1.
        """
        esquerda, direita = 0, len(lista) - 1
        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            if lista[meio] == alvo:
                return meio
            elif lista[meio] < alvo:
                esquerda = meio + 1
            else:
                direita = meio - 1
        return -1
