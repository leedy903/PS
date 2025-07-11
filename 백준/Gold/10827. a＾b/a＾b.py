import sys
input = sys.stdin.readline
from decimal import Decimal, getcontext

a, b = map(str, input().strip().split())

getcontext().prec = 1101
print("{0:f}".format(Decimal(a)**int(b)))