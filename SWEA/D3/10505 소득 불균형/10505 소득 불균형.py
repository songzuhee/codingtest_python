import sys
input = sys.stdin.readline

t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))

    avg_income = 0
    result = 0

    for i in range(n):
        result += arr[i]
    avg_income = result // n

    min_count = 0
    for i in range(n):
        if avg_income >= arr[i]:
            min_count += 1
    print('#{} {}'.format(test_case, min_count))

