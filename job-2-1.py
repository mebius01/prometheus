#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math;

x=float(sys.argv[1]);
y=float(sys.argv[2]);
z=float(sys.argv[3]);

part1=(1 / (z * math.sqrt(2 * math.pi)));
part2=math.exp( - ((x - y)**2) / (2*(z**2)));

print(part1*part2)
