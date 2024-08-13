n = int(input())
answer = 0

for i in range(1, n + 1):
    for j in range(i, n - i + 1):
        k = n - i - j
        if i + j > k and k >= j:
            answer += 1
print(answer)


# second approach: a+b+c=n -> a+b = n-c -> a+b>c -> n-c>c -> n/2>c

n = int(input())
n1 = n//2+1
ans = 0

for a in range(n1):
    for b in range(a, n1):
        c = n-a-b
        if a+b+c == n and a+b > c:
            ans += 1
print(ans)
