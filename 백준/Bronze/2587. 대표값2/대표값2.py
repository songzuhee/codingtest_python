import sys
input = sys.stdin.readline

arr = []
avg = 0

for i in range(5):
    a = int(input())
    arr.append(a)
    avg += a
    arr.sort()

print(avg//5)
print(arr[2])