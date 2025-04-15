def bubble_sort(lista):
	n = len(lista)	
	
	for i in range(n - 1 , 0 , -1):
		trocou = False
		for j in range(i):
			if lista[j] > lista[j + 1]:
				lista[j] , lista[j + 1] = lista[j + 1] , lista[j]
				trocou = True
		if not trocou:
			return

lista = [12, 1, 2, 3, 4, 5, 7, 6, 8, 9, 11, 10]	
bubble_sort(lista)
print(lista)
