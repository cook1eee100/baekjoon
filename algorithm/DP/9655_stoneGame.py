import sys
input = sys.stdin.readline

n = int(input())

if n%2==0:
    print("CY")
else:
    print("SK")





"""
sk, cy

1   sk  sk1
2   cy  sk1 cy1
3   sk  sk3
4   cy  sk1 cy1 sk1 cy1,    sk3 cy1,    sk1 cy3
5   sk  sk3 cy1 sk1,
"""