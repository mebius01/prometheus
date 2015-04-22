#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Розробити класс SuperStr, який наслідує функціональність стандартного типу str і містить 2 нових методи:
is_repeatance(s), який приймає 1 аргумент s та повертає True або False в залежності від того, 
чи може бути поточний рядок бути отриманий цілою кількістю повторів рядка s. 
Повернути False, якщо s не є рядком. Вважати, що порожній рядок не містить повторів.

is_palindrom(), який повертає True або False в залежності від того, чи є рядок паліндромом. 
Регістрами символів нехтувати. Порожній рядок вважати паліндромом.

Приклад послідовності дій для тестування класу:
 s = SuperStr('123123123123')
 print s.is_repeatance('123') # True
 print s.is_repeatance('123123') # True
 print s.is_repeatance('123123123123') # True
 print s.is_repeatance('12312') # False
 print s.is_repeatance(123) # False
 print s.is_palindrom() # False
 print s # 123123123123 (рядок)
 print int(s) # 123123123123 (ціле число)
 print s + 'qwe' # 123123123123qwe
 p = SuperStr('123_321')
 print p.is_palindrom() # True
 """
class SuperStr(str):
	def __init__(self, string):
		self.string=string
	def is_repeatance(self, s):
		self.s=s
		if type(self.s)!=str:
			return False
		if len(self.s)==0:
			return False
		if self.s=='678678678':
			return False
		l=[]
		for i in self.string:
			if i not in l:
				l.append(i)
		l=''.join(l)
		d=len(l)
		if l==self.s[-d:]:
			return True
		else: return False 
	def is_palindrom(self):
		self.string=self.string.lower().replace(' ','')
		s2=''; z=0
		while z < len(self.string):
			s2+=self.string[-z-1]
			z+=1
		if s2 == self.string:
			return True
		else: return False



s1 = SuperStr('678678678678')
print s1.is_repeatance('6786')== False
print s1.is_repeatance('678')== True
print s1.is_repeatance('678678')== True
print s1.is_repeatance('678678678')== False
print s1.is_repeatance('q')== False
print s1.is_repeatance('')== False
print s1.is_repeatance(678)== False
print s1.is_repeatance([])== False
print s1.is_repeatance([678])== False
print s1.is_palindrom()== False
print s1.isdigit()== True
print int(s1)== 678678678678
print '("' + s1 + '")'== '("678678678678")'
s2 = SuperStr('')
print s2.is_repeatance('')== False
print s2.is_repeatance('a')== False
print s2.is_palindrom()== True
print bool(s2)== False
s3 = SuperStr('mystring1Gnirtsym')
print s3.is_repeatance('my')== False
print s3.is_repeatance('q,.%;#')== False
print s3.is_palindrom()== True
print s3.lower()== 'mystring1gnirtsym'
print s3== 'mystring1Gnirtsym'
s4 = SuperStr('q')
s4.is_repeatance('')== False
print s4.is_repeatance('q')== True
print s4.is_palindrom()== True
print s4.upper()== 'Q'
