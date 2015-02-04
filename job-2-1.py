#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Вхідні дані: 2 невід'ємних дійсних числа a та b -- аргументи командного рядка. b не дорівнює 0.

Вихідні дані: дійсне число -- результат обчислення формули  
"""
import sys, math;

x=float(sys.argv[1]);
y=float(sys.argv[2]);
z=float(sys.argv[3]);

part1=(1 / (z * math.sqrt(2 * math.pi)));
part2=math.exp( - ((x - y)**2) / (2*(z**2)));

print(part1*part2)
