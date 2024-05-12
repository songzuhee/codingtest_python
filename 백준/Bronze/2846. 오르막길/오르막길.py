import sys
input = sys.stdin.readline

n = int(input())

road = list(map(int, input().split()))
result = []
a = 0

for i in range(n-1):
    if road[i] < road[i+1]:
        a += road[i+1] - road[i]
    else:
        result.append(a)
        a = 0

result.append(a)
print(max(result))