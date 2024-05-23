import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    print(arr[3-1])