def solution(n):
    arr = list(str(n))
    result =0
    for i in range(len(arr)):
        result += int(arr[i])
    result = result + n
    return result

results = set()
for i in range(10000):
    results.add(solution(i))
for j in range(1, 10001):
    if j not in results:
        print(j)