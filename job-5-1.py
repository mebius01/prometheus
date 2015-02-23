#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Розробити функцію clean_list(list_to_clean), 
 яка приймає 1 аргумент -- список будь-яких значень (рядків, цілих та діясних чисел) довільної довжини,
 та повертає список, який складається з тих самих значень, але не містить повторів елементів. 
 Це значить, що у випадку наявності значення в початковому списку в кількох екземплярах 
 перший "екземпляр" значення залишається на своєму місці, а другий, третій та ін. видаляються.

Наприклад
 Виклик функції: clean_list([1, 1.0, '1', -1, 1])
 Повертає: [1, 1.0, '1', -1]
 Виклик функції: clean_list(['qwe', 'reg', 'qwe', 'REG'])
 Повертає: ['qwe', 'reg', 'REG']
 Виклик функції: clean_list([32, 32.1, 32.0, -123])
 Повертає: [32, 32.1, 32.0, -123]
 """
input_list = [[32, 32.1, 32.0, -123]]
def clean_list(l):
	output_list = []
	for i in l:
		typ=type(i)
		if i not in output_list:
			output_list.append(i)
		if i in output_list:
			if type(i) != type(output_list[output_list.index(i)]):
				output_list.append(typ(i))
	return(output_list)

print clean_list(input_list)
