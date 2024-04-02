#NOSSO ARQUIVOOO PODE FAZER COMMIT 

class Ordenacao:
    
    ## bubble sort
    @staticmethod
    def bubble_sort(lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista

    ## selection sort
    @staticmethod
    def selection_sort(lista):
        n = len(lista)
        for i in range(n):
            menor_indice = i
            for j in range(i+1, n):
                if lista[j] < lista[menor_indice]:
                    menor_indice = j
            lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
        return lista

    ## insertion sort
    @staticmethod
    def insertion_sort(lista):
        for i in range(1, len(lista)):
            chave = lista[i]
            j = i-1
            while j >= 0 and lista[j] > chave:
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = chave
        return lista
    
        ## merge sort
    @staticmethod
    def merge_sort(lista):
        if len(lista) <= 1:
            return lista
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]
        
        esquerda = Ordenacao.merge_sort(esquerda)
        direita = Ordenacao.merge_sort(direita)
        
        return Ordenacao.merge(esquerda, direita)