n = int(input())
ans = 0

for a in range(n):
    for b in range(a, n):
        for c in range(b, n):
            if a+b+c == n and a+b > c:
                ans += 1
print(ans)
