import sys
input = sys.stdin.readline

n = int(input())

km = list(map(int, input().split()))
l = list(map(int, input().split()))

result = 0
minPrice = l[0]

for i in range(n-1):
    if minPrice > l[i]:
        minPrice = l[i]
    result += minPrice*km[i]
print(result)