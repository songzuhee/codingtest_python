import sys
input = sys.stdin.readline

c = int(input())

for _ in range(c):
    arr = list(map(int, input().split()))

    student_avg = sum(arr[1:])/arr[0]

    cnt = 0
    for i in arr[1:]:
        if i > student_avg:
            cnt += 1
    print('{:.3f}{}'.format((cnt/arr[0]) * 100,'%'))