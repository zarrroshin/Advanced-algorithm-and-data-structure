n = int(input())
answer = 0

for i in range(1, n + 1):
    for j in range(i, n - i + 1):
        k = n - i - j
        if i + j > k and k >= j:
            answer += 1
print(answer)
