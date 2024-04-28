import sys
input = sys.stdin.readline

def fibo(n):
    if n == 0 or n == 1:
        return n

    arr = [0 for _ in range(n + 1)]

    arr[1] = 1

    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[-1] % 1234567

n = int(input())
print(fibo(n))