import sys
input = sys.stdin.readline

t = int(input())

for test_case in range(1, t+1):
    sum_num = 0
    result = 0
    arr = list(map(int, input().split()))

    max_num = max(arr)
    min_num = min(arr)

    arr.remove(max_num)
    arr.remove(min_num)

    for i in range(len(arr)):
        sum_num += arr[i]
    print('#{} {}'.format(test_case, round(sum_num / 8)))