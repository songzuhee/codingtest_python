import sys
input = sys.stdin.readline

for test_case in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))
    result = 0

    for i in range(dump):
        # 오름차순 정렬
        arr.sort()
        arr[0] = arr[0]+1
        arr[-1] = arr[-1]-1
        arr.sort()
        result = arr[-1] - arr[0]
    print('#{} {}'.format(test_case, result))
