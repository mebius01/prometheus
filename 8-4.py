#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Розробити функцію make_sudoku(size), 
 яка приймає 1 аргумент -- додатнє ціле число (1 <= size <= 42), 
 та повертає список списків -- квадратну матрицю, що представляє судоку розмірності size.

Судоку розмірності X являє собою квадратну матрицю розмірністю X**2 на X**2, 
розбиту на X**2 квадратів розмірністю X на X, заповнену цілими числами таким чином, 
щоб кожна вертикаль, кожна горизонталь та кожний квадрат містили всі числа від 1 до X**2 
включно без повторів.

Наприклад, судоку розмірності 3 може виглядати наступним чином:

-- квадрат 9х9 (3**2 = 9), який складається з 9 квадратів 3х3. 
В кожній вертикалі розміщені різні числа від 1 до 9. 
Те саме стосується кожної горизонталі та кожного внутрішнього квадрату.

Дане завдання не має єдиного вірного розв'язку -- ваша функція повинна повертати результат, 
який задовольняє умові, за відведений час.

Тести із некоректними даними не проводяться

Приклад вхідних і вихідних даних:
print make_sudoku(1) # [[1]]
print make_sudoku(2) # [[1,2,3,4],[3,4,1,2],[2,1,4,3],[4,3,2,1]]
print make_sudoku(3) # 

[3,5,8,1,2,7,6,4,9],
[6,7,4,5,8,9,3,2,1],
[2,1,9,3,4,6,5,7,8],
[9,8,6,7,1,4,2,5,3],
[4,3,1,2,6,5,8,9,7],
[7,2,5,9,3,8,1,6,4],
[1,6,3,4,7,2,9,8,5],
[8,9,7,6,5,1,4,3,2],
[5,4,2,8,9,3,7,1,6]

"""
def make_sudoku(size):
	size=size**2
	import random
	l=[]; y=0; etal=range(1,size+1); random.shuffle(etal)
	while len(l) < size:
		for i in etal:
			l.append([i])

	while y < size:
		random.shuffle(etal)
		for i in etal:
			if i not in l[y]:
				l[y].append(i)
		y+=1
	return l


print make_sudoku(42)

	#~ def ran(s):
		#~ l=[]
		#~ while len(l) < s:
			#~ x=random.randint(1,s)
			#~ if x not in l:
				#~ l.append(x)
		#~ return l
	#~ while (y < size):
		#~ x=ran(size)
		#~ if x[0] not in etal:
			#~ etal.append(x[0])
			#~ l_g.append(x)
		#~ y+=1
	#~ 
"""
def check_sudoku(l):
	n = len(l)
	if n == 1 and l == [[1]]:
	    return True
	
	for i in xrange(n):
	    for j in xrange(n):
	        v = l[i][j]
	        for t in xrange(j + 1, n):
	            if l[i][t] == v:
	                return False
	        for t in xrange(i + 1, n):
	            if l[t][j] == v:
	                return False
	
	nn = int(math.sqrt(n))
	for i in xrange(nn):
	   for j in xrange(nn):
	    t = j * nn
	    lt = []
	    for x in xrange(nn):
	        lt += l[i * nn + x][t : t + nn]
	    for i1 in xrange(n):
	        for j1 in xrange(i1 + 1, n):
	            if lt[i1] == lt[j1]:
	                return False;
	return True
def make_sudoku(size):
"""
