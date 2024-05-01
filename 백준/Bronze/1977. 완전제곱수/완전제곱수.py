import sys
input = sys.stdin.readline

m = int(input())
n = int(input())
sum = 0
min = []

for i in range(101):
    if n >= i*i >= m:
        min.append(i*i)
        sum += i*i

if sum == 0:
    print(-1)
elif sum != 0:
    print(sum)
    print(min[0])
