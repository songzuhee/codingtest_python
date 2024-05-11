import sys
input = sys.stdin.readline

length = []
a = 0
b = 0

# 원소들 중에서 두개의 합이 100이라면 그 원소를 빼고 구하면 됨.
for _ in range(9):
    length.append(int(input()))
# print(length)
total = sum(length)

for i in range(9):
    for j in range(i+1, 9):
        if total - (length[i]+length[j]) == 100:
            a = length[i]
            b = length[j]
            break
length.remove(a)
length.remove(b)
length.sort()

for i in length:
    print(i)