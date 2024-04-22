import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

total = a * b * c

arr = [0 for _ in range(10)]

n_list = list(map(int, str(total)))

for i in range(len(n_list)):
    arr[n_list[i]] += 1

for i in arr:
    print(i)