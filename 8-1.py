#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Розробити класс CombStr для представлення рядка символів.

Забезпечити наступні методи класу:
конструктор, який приймає 1 аргумент -- рядок string.
метод count_substrings(length), який приймає 1 аргумент -- невід'ємне ціле число length, 
та повертає ціле число -- кількість всіх різних підрядків довжиною length, 
що містяться в рядку string.

Тести із некоректними даними не проводяться. 

Послідовність символів substring вважається підрядком рядка string, 
якщо її можна отримати зі string шляхом відкидання символів з початку та/або з кінця рядка. 
Наприклад 'asd' є підрядком 'asdfg', а 'fgh' -- ні. Вважати, що порожніх підрядків не буває, 
тому для length=0 повертати 0.

Приклад послідовності дій для тестування класу:
s0 = CombStr('qqqqqqweqqq%')
print s0.count_substrings(0) # 0
print s0.count_substrings(1) # 4
print s0.count_substrings(2) # 5
print s0.count_substrings(5) # 7
print s0.count_substrings(15) # 0
"""
class CombStr(object):
	def __init__(self, string):
		self.string=string
	def count_substrings(self, length):
		self.length=length
		if self.length == 0:
			return 0
		a=0;l=[]
		while self.length < len(self.string)+1:
			if self.string[a:self.length] not in l:
				l.append(self.string[a:self.length])
			a+=1; self.length+=1
		return len(l)

s0 = CombStr('qqqqqqweqqq%')
print s0.count_substrings(0) , 0
print s0.count_substrings(1) , 4
print s0.count_substrings(2) , 5
print s0.count_substrings(5) , 7
print s0.count_substrings(15) , 0
s4 = CombStr('29389efj s9fbsyaedg dBD QYDUEHWFUHB&*#(@)(#!')
print s4.count_substrings(1)
s1  = CombStr('')
print s1.count_substrings(0), 0
print s1.count_substrings(1), 0
s2  = CombStr('?')
print s2.count_substrings(0), 0
s5  = CombStr("A taste of honey. Tasting much sweeter than wine. I dream of your first kiss. And then I feel upon my lips again. A taste of honey. Tasting much sweeter than wine. I will return, yes I will return. I'll come back for the honey and you. Yours was the kiss that awoke my heart. There lingers still, though we're far apart. That taste of honey. Tasting much sweeter than wine. Oh I will return, yes I will return. I'll come back (He'll come back). for the honey (For the honey). and you")
print s5.count_substrings(7)


"""
Правильно
Виклик: s1  = CombStr('')
Відповідь:
Помилки
Неправильно обрахований результат. Для виклику 
s1.count_substrings(0) 
очікуваний результат: 0. Ваш результат: '1'
Ваша відповідь:
1
Правильна відповідь:
0
Правильно
Виклик:
s1.count_substrings(1)
Відповідь:
0
Правильно
Виклик: s2  = CombStr('?')
Відповідь:
Помилки
Неправильно обрахований результат. Для виклику 
s2.count_substrings(0) 
очікуваний результат: 0. Ваш результат: '1'
Ваша відповідь:
1
Правильна відповідь:
0
Правильно
Виклик:
s2.count_substrings(1)
Відповідь:
1
Правильно
Виклик:
s2.count_substrings(2)
Відповідь:
0
Правильно
Виклик: s3  = CombStr('qweqweqwe')
Відповідь:
Правильно
Виклик:
s3.count_substrings(1)
Відповідь:
3
Правильно
Виклик:
s3.count_substrings(2)
Відповідь:
3
Правильно
Виклик:
s3.count_substrings(3)
Відповідь:
3
Правильно
Виклик:
s3.count_substrings(4)
Відповідь:
3
Правильно
Виклик:
s3.count_substrings(9)
Відповідь:
1
Правильно
Виклик:
s3.count_substrings(10)
Відповідь:
0
Правильно
Виклик: s4  = CombStr('29389efj s9fbsyaedg dBD QYDUEHWFUHB&*#(@)(#!')
Відповідь:
Правильно
Виклик:
s4.count_substrings(1)
Відповідь:
30
Правильно
Виклик:
s4.count_substrings(2)
Відповідь:
43
Правильно
Виклик:
s4.count_substrings(5)
Відповідь:
40
Правильно
Виклик:
s4.count_substrings(15)
Відповідь:
30
Правильно
Виклик: s5  = CombStr("A taste of honey. Tasting much sweeter than wine. I dream of your first kiss. And then I feel upon my lips again. A taste of honey. Tasting much sweeter than wine. I will return, yes I will return. I'll come back for the honey and you. Yours was the kiss that awoke my heart. There lingers still, though we're far apart. That taste of honey. Tasting much sweeter than wine. Oh I will return, yes I will return. I'll come back (He'll come back). for the honey (For the honey). and you")
Відповідь:
Правильно
Виклик:
s5.count_substrings(1)
Відповідь:
34
Правильно
Виклик:
s5.count_substrings(7)
Відповідь:
311
Правильно
Виклик:
s5.count_substrings(14)
Відповідь:
355
Правильно
Виклик:
s5.count_substrings(21)
Відповідь:
372
Правильно
Виклик:
s5.count_substrings(45)
Відповідь:
420
"""
