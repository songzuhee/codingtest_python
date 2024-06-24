import sys
input = sys.stdin.readline

a, p = map(int, input().split())
results = [a]

while True:
    n = list(str(a))
    result = 0

    for i in range(len(n)):
        result += int(n[i])**p

    if result in results:
        results = results[:results.index(result)]
        break

    results.append(result)
    a = result

print(len(results))