# 이건 앞에서부터 구한 코드 -> 시간초과 뜸, 테스트 케이스 0개 통과 .. ^^
import sys
input = sys.stdin.readline

t = int(input())
# result = []
#
# for i in range(1, t+1):
#     n = int(input())
#     result = list(map(int, input().split()))
#     benefit = 0
#
#     for j in range(len(result)):
#         max_cost = max(result[j::])
#
#         if result[j] < max_cost:
#             benefit += max_cost - result[j]
#     print(benefit)

result = []
max_cost = 0

for _ in range(1, t+1):
    n = int(input())
    result = list(map(int, input().split()))
    benefit = 0

    max_cost = result.pop()

    for i in reversed(result):
        if i > max_cost:
            max_cost = i
        else:
            benefit += max_cost - i
    print(benefit)
