import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    arr = []
    s = list(input().split())
    for j in s:
        arr.append(j[::-1])
    print(*arr)