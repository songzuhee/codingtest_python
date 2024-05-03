import sys
input = sys.stdin.readline

# 주차요금 a b c
a, b, c = map(int, input().split())

bus = [0] * 101
result = 0

for _ in range(3):
    s, e = map(int, input().split())
    for i in range(s, e):
        bus[i] += 1

for i in bus:
    if i == 1:
        result += a
    elif i == 2:
        result += 2*b
    elif i == 3:
        result += 3*c
print(result)