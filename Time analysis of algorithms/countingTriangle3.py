n = int(input())
answer = 0

for a in range(n//3+1):
    answer = answer + (n-3*a)//2 - max(0, n//2-2*a+1) + 1
print(answer)
