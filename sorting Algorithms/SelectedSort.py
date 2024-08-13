n = int(input())
seq = list(map(int, input().split()))

for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if seq[i] > seq[j]:
            min_index = j
    seq[i], seq[min_index] = seq[min_index], seq[i]
print(*seq, " ")
