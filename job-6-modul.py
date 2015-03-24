#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
Розробити функцію convert_n_to_m(x, n, m),
яка приймає 3 аргументи -- ціле число (в системі числення з основою n) або рядок x, що представляє таке число, 
та цілі числа n та m (1 <= n, m <= 36),
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

def convert_n_to_m(x, n, m):
	x=str(x)
	if x[0]=='0':
		x=x[1:]
	ret_string=''
	def convert_in_10(x, y): # конвертирует из 2-9 в 10-чную
		x=str(x); z=1
		lett={'0':0, '1':1, '2':2, '3':3, '4':4, 
			'5':5, '6':6, '7':7, '8':8, '9':9, 
			'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 
			'F':15, 'G':16, 'H':17, 'I':18, 'J':19, 
			'K':20, 'L':21, 'M':22, 'N':23, 'O':24, 
			'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 
			'U':30, 'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35}
		rec=(int(lett.get((x[0]))))
		while z < len(x):
			rec=(rec*y+(int(lett.get((x[z])))))
			z+=1
		return rec
	def convert_from_10(x, y): # кконвертирует из 10-чной в 2-9
		list_10=[]; fract=None; s=''
		lett={0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 
			5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 
			10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 
			15:'F', 16:'G', 17:'H', 18:'I', 19:'J', 
			20:'K', 21:'L', 22:'M', 23:'N', 24:'O', 
			25:'P', 26:'Q', 27:'R', 28:'S', 29:'T', 
			30:'U', 31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z'}
		def f(i, l):
			if i in l:
				return l.get(i)
		def u(f, d):
			return(int(round(f*d)))
		while x >= y:
			x=float(x)/y; x=str(x); x=x.split('.'); fract='0.'+(x[1]); fract=float(fract); x=float(x[0]); 
			list_10.append(f(u(fract, y), lett))
			if x < y:
				list_10.append(f(int(x), lett)); list_10.reverse()
		for i in list_10:
			s=s+i
		return s
	try:
		if m == 1:
			for i in range(convert_in_10(x, n)):
				ret_string+='0'
			return ret_string
		elif convert_from_10(convert_in_10(x, n), n) == str(x):
			return convert_from_10(convert_in_10(x, n), m)
		else:
			return False
	except TypeError:
		return False

print convert_n_to_m(0, 10, 2), '0' #string index out of range
print convert_n_to_m(000, 10, 2), '0' #string index out of range
print convert_n_to_m('000', 10, 2), '0'
print convert_n_to_m('000ZZZZ', 36, 13), '46A672'
print convert_n_to_m('qweasd', 33, 36), 'HGPEYJ'
print convert_n_to_m('123123123123123123123', 11, 16), '2C09BC518E8048D23A'
print convert_n_to_m(123123123123123123123, 11, 16), '2C09BC518E8048D23A'
print convert_n_to_m(123123123123123123123, 10, 10), '123123123123123123123'
print convert_n_to_m('bnh34521', 31, 14), '119337DC2BC'
print convert_n_to_m('bnh34521', 11, 14), 'False'

print convert_n_to_m([123], 4, 3), 'False'
print convert_n_to_m("0123", 5, 6), '102'
print convert_n_to_m("123", 3, 5), "False"
print convert_n_to_m(123, 4, 1)=='000000000000000000000000000'
print convert_n_to_m(-123.0, 11, 16), 'False'
print convert_n_to_m("A1Z", 36, 16), '32E7'

