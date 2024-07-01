import sys

input = sys.stdin.readline

# 5 4 3 2 1
# 3, 5 ->  3 + 2 + 1 = 6

def prefix_sum(arr):
    #누적합을 담을 배열 prefixSum
    prefixSum = [0] * len(arr)
    prefixSum[0] = arr[0]

    for i in range(1, len(arr)):
        prefixSum[i] = prefixSum[i-1] + arr[i]
    return prefixSum

n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefixSum = prefix_sum(arr)

for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        result = prefixSum[b - 1]
    else:
        result = prefixSum[b - 1] - prefixSum[a - 2]
    print(result)