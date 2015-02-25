#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Розробити функцію count_holes(n), 
яка приймає 1 аргумент -- ціле число або рядок, який містить ціле число,
та повертає ціле число -- кількість "отворів" у десятковому записі цього числа друкованими цифрами 
(вважати, що у "4" та у "0" по одному отвору), або рядок ERROR, якщо переданий аргумент не задовольняє вимогам: 
є дійсним або взагалі не числом.

Незначущими нулями на початку запису числа, якщо такі є, нехтувати.

Наприклад
Виклик функціїі: count_holes('123')
Повертає: 0
Виклик функціїі: count_holes(906)
Повертає: 3
Виклик функціїі: count_holes('001')
Повертає: 0
Виклик функціїі: count_holes(-8)
Повертає: 2
Виклик функціїі: count_holes(-8.0)
Повертає: ERROR
"""
def count_holes(n):
	glob_dic={0:1, 4:1, 6:1, 8:2, 9:1, -4:1, -6:1, -8:2, -9:1}; s=''; con=0
	if isinstance(n, float):
		return('ERROR')
	elif isinstance(n, str):
		for i in n:
			if i.isdigit():
				i=int(i)
				if i in glob_dic:
					s=s+str(i)
	elif isinstance(n, int):
		n=str(n)
		for i in n:
			if i.isdigit():
				i=int(i)
				if i in glob_dic:
					s=s+str(i);
	def con(x):
		z_len=len(x)
		while z_len > 0:
			if x[0] == '0':
				x=x[1:]
			z_len-=1
		return(x)
	return(len(con(s)))
print count_holes('123')
print count_holes(906)
print count_holes('001')
print count_holes(8)
print count_holes(-8.0)


#~ n='1'
#~ glob_dic={0:1, 4:1, 6:1, 8:2, 9:1}; con=0; s=''
#~ if isinstance(n, float):
	#~ print 'ERROR'
#~ elif isinstance(n, str):
	#~ for i in n:
		#~ if i.isdigit():
			#~ i=int(i)
			#~ if i in glob_dic:
				#~ s=s+str(i)
				#~ con+=1
#~ print s, con

