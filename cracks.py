#!/usr/bin/python
from gmpy2 import isqrt
from sys import exit

e = 0x10001
N = 168099244427122904039722681464047291363373983875$
delta = 50

for x in range(1, e):
    q_approx = isqrt(N*x/e)
    for q in range(q_approx - delta, q_approx + delta):
        if N % q == 0:
            print 'P:', N/q
            print 'Q:', q
            exit(0)
