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
	glob_dic={0:1, 4:1, 6:1, 8:2, 9:1}; s=''; con=0
	if isinstance(n, float):
		return('ERROR')
	elif isinstance(n, str):
		for i in n:
			if i.isdigit():
				i=int(i)
				if i in glob_dic:
					s=s+str(i)
					con+=glob_dic.get(i)
					if s[0] == '0':
						con-=1
						s=s[1:]
						 
					
	elif isinstance(n, int):
		n=str(n)
		for i in n:
			if i.isdigit():
				i=int(i)
				if i in glob_dic:
					s=s+str(i);
					con+=glob_dic.get(i)
					if s[0] == '0':
						con-=1
						s=s[1:]
	return(con, s)

count_holes(0), "1"
count_holes('000000000010'), "1" 
count_holes(888888888888888888888), "42"
count_holes(-888888888888888888888), "42"
print count_holes('888888888888888888888.0'), "ERROR"
count_holes(''), "ERROR"
count_holes(69L), "2"
count_holes([1]), "ERROR"
count_holes(None), "ERROR"
count_holes('qq'), "ERROR"
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

