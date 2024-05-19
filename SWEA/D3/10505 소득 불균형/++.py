# 코드 길이가 길어져서 다른 사람 코드도 참고해봤다.
# 평균 소득을 구할 때 반복문을 사용하지 않고,

import sys
input = sys.stdin.readline

t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))

    min_count = 0

    avg_income = sum(arr) // n

    for i in arr:
        if i <= avg_income:
            min_count += 1
    print('#{} {}'.format(test_case, min_count))

# 이방식으로 하니 220ms -> 184ms 으로 단축되었다.