import sys
input = sys.stdin.readline

a, b = list(map(int, input().split()))
print(max(str(a)[::-1], str(b)[::-1]))