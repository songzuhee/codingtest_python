import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result = []

arr.sort(reverse=True)
for i in range(n):
    result.append(i+1+arr[i])

print(max(result)+1)