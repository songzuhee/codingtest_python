import sys
input = sys.stdin.readline

n = int(input())
arr = []
result = 0

for _ in range(n):
    arr.append(int(input()))

result = 0
for i in range(n-1, 0,-1):
    if arr[i] <= arr[i-1]:
        result += arr[i-1] - arr[i]+1
        arr[i-1] = arr[i]-1
print(result)