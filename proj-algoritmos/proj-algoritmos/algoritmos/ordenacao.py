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