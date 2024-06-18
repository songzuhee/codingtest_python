import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

total = 0
for i in range(n):
    max_b = max(b)
    total += a[i] * max_b
    b.remove(max_b)
print(total)