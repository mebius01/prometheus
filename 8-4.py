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
	a=size; b=size
	size=size**2
	import random
	l=[]; y=0; etal=range(1,size+1); random.shuffle(etal)

	while len(l) < size:
		while len(l) < a: #<---
			l.append(etal)
			etal=etal[b:] + etal[:b]
		etal=etal[1:] + etal[:1]
		a+=b

	return l

print make_sudoku(3)

def check_sudoku(l):
	import math
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

print check_sudoku(make_sudoku(2))
print check_sudoku(make_sudoku(3))
print check_sudoku(make_sudoku(5))
print check_sudoku(make_sudoku(10))
print check_sudoku(make_sudoku(42))

"""

Правильно

Виклик:
is_sudoku( make_sudoku(1) , 1)

Відповідь:

    True

Помилки

Неправильно обрахований результат. Для виклику 
is_sudoku( make_sudoku(3) , 3) 
очікуваний результат: True. Ваш результат: 'False'

Ваша відповідь:

    False

Правильна відповідь:

    True

Помилки

Неправильно обрахований результат. Для виклику 
is_sudoku( make_sudoku(5) , 5) 
очікуваний результат: True. Ваш результат: 'False'

Ваша відповідь:

    False

Правильна відповідь:

    True

Помилки

Неправильно обрахований результат. Для виклику 
is_sudoku( make_sudoku(10) , 10) 
очікуваний результат: True. Ваш результат: 'False'

Ваша відповідь:

    False

Правильна відповідь:

    True

Помилки

Неправильно обрахований результат. Для виклику 
is_sudoku( make_sudoku(42) , 42) 
очікуваний результат: True. Ваш результат: 'False'

Ваша відповідь:

    False

Правильна відповідь:

    True

"""

