import sys
input = sys.stdin.readline

n = int(input())
count = 0

# 성을 담을 리스트
name = []

for _ in range(n):
    a = input().rstrip()
    name.append(a[0])

n_list = []
for i in name:
    if name.count(i) >= 5:
        n_list.append(i)


if len(n_list) > 0:
    print(''.join(sorted(set(n_list))))
else:
    print('PREDAJA')