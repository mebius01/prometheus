#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
Розробити функцію convert_n_to_m(x, n, m),
яка приймає 3 аргументи -- ціле число (в системі числення з основою n) або рядок x, що представляє таке число, та цілі числа n та m (1 <= n, m <= 36),
та повертає рядок -- представлення числа х у системі числення m.

У випадку, якщо аргумент х не є числом або рядком, 
або не може бути представленням цілого невід'ємного числа в системі числення з основою n, 
повернути логічну константу False.

В системах числення з основою більше десяти для позначення розрядів із значенням більше 9 
використовувати літери латинського алфавіту у верхньому регістрі від A до Z.

Вважати, що в одиничній системі числення число записується відповідною кількістю нулів.

Наприклад
Виклик функції: convert_n_to_m([123], 4, 3)
Повертає: False
Виклик функції: convert_n_to_m("0123", 5, 6)
Повертає: 102
Виклик функції: convert_n_to_m("123", 3, 5)
Повертає: False
Виклик функції: convert_n_to_m(123, 4, 1)
Повертає: 000000000000000000000000000
Виклик функції: convert_n_to_m(-123.0, 11, 16)
Повертає: False
Виклик функції: convert_n_to_m("A1Z", 36, 16)
Повертає: 32E7
"""
#~ def r(x):
	#~ return (((((3 * x + 5) * x + 0) * x + 2) * x + 1) * x + 4)
'''def f(x, y):
	x=str(x); z=1; rec=int(x[0]) 
	while z < len(x):
		rec=(rec*y+int(x[z]))
		z+=1
	return x, rec
for i in range(1,16):
	print "в =>", i, f(-123, i), "<= в 10-й сист."

#~ http://planetcalc.ru/375/ cal
#~ http://habrahabr.ru/post/124395/ Основы систем счисления
#~ http://www.tryobj.com/24-varianty-perevoda-chisel-iz-odnoy-sistemy-v-druguyu.html Варианты перевода чисел из одной системы в другую
'''
def x_convert_10(x, y):
	list_10=[]; fract=None; s=''
	def u(f, d):
		return(int(round(f*d)))
	while x >= y:
		x=float(x)/y; x=str(x); x=x.split('.'); fract='0.'+(x[1]); fract=float(fract); x=float(x[0]); 
		list_10.append(u(fract, y))
		if x < y:
			list_10.append(int(x)); list_10.reverse()
	for i in list_10:
		i=str(i); s=s+i
	return s
print x_convert_10(3465, 7)







