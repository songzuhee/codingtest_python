import sys
input = sys.stdin.readline

n = int(input())
arr = []
result = 0

for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

for i in range(2, len(arr), 3):
    result += arr[i]
print(sum(arr) - result)