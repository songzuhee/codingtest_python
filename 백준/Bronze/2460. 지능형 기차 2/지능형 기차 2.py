import sys
input = sys.stdin.readline

train = []
c = 0

for _ in range(10):
    a, b = map(int, input().split())
    c = (c - a) + b
    train.append(c)
print(max(train))