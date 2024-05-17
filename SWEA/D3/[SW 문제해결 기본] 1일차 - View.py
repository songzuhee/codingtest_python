import sys
input = sys.stdin.readline

for test_case in range(1, 3):
    n = int(input())
    arr = list(map(int, input().split()))

    # 조망권 확보된 세대의 수
    result = 0

    for i in range(2, n-2):
        right = 0
        left = 0

        # 현재 건물이 양쪽 2개의 건물보다 크다면
        if arr[i] > arr[i+1] and arr[i] > arr[i+2] and arr[i] > arr[i-1] and arr[i] > arr[i-2]:
            max_value = 0

            right = max(arr[i+1], arr[i+2])
            left = max(arr[i-1], arr[i-2])
            max_apart = max(left, right)

            result += arr[i] - max_apart

    print('#{} {}'.format(test_case, result))
