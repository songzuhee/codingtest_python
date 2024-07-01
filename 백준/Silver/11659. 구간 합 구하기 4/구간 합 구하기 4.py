import sys

input = sys.stdin.readline

# 5 4 3 2 1
# 3, 5 ->  3 + 2 + 1 = 6

n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefixSum = [0] * (len(arr)+1)
for i in range(1, len(arr) +1):
    prefixSum[i] = prefixSum[i-1]+arr[i-1]

for _ in range(m):
    a, b = map(int, input().split())
    print(prefixSum[b] - prefixSum[a-1])
