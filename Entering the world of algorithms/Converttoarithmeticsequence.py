# solution
n, k = map(int, input().split())
seq = list(map(int, input().split()))
minimum = min(seq)
maximum = max(seq)
var = 1000*1000*1000
for i in range(minimum-(n-1)*k, maximum+1):
    t = 0
    for m in range(n):
        t += abs((i+k*m)-seq[m])
    var = min(var, t)
print(var)


# my first approach:
# n, k = map(int, input().split())
# seq = list(map(int, input().split()))
# numOfOperation = []

# for num in range(len(seq)):
#     alternative = seq[num]+k
#     count = 0
#     for i in range(num+1, len(seq)):
#         a = abs(seq[i] - alternative)
#         count += a
#         alternative += k
#     alternative = seq[num]-k
#     for i in range(num-1, -1, -1):
#         a = abs(seq[i] - alternative)
#         count += a
#         alternative -= k
#     numOfOperation.append(count)
# print(min(numOfOperation))
