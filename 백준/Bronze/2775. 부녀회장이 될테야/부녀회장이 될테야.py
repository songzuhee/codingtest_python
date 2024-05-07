import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input()) #층
    n = int(input()) #호
    apt = [i for i in range(1, n+1)] #0층

    for i in range(k):
        for j in range(1, n):
            apt[j] += apt[j-1]
    print(apt[n-1])