import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = []

for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

cnt = 0
for i in range(n):
    if k >= arr[i]:
        a = k // arr[i]
        cnt += a
        k -= arr[i] * a
print(cnt)