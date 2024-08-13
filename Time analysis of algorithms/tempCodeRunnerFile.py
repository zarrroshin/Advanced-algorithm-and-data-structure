n = int(input())
n1=n//2+1
ans = 0

for a in range(n1):
    for b in range(a,n1):
        for c in range(b,n1):
            if a+b+c ==n and a+b>c : 
                ans +=1
print(ans)

