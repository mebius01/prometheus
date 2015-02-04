#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 ПРАКТИЧНЕ ЗАВДАННЯ №3.1
(2 можливих балів)

Вхідні дані: 3 дійсних числа a, b, c. Передаються в програму як аргументи командного рядка.

Результат роботи: рядок "triangle", якщо можуть існувати відрізки з такою довжиною 
та з них можна скласти трикутник, або "not triangle" -- якщо ні.

Любая сторона треугольника меньше суммы двух других сторон и больше
их разности ( a < b + c,  a > b – c;  b < a + c,  b > a – c;  c < a + b,  c > a – b ).
"""

import sys
a=float(sys.argv[1])
b=float(sys.argv[2])
c=float(sys.argv[3])
if (b + c) > a and (a + c) > b and (a + b) > c:
	print "triangle"
else:
	print "not triangle"

