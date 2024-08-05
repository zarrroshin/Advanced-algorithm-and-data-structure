# solution

n = int(input())
a = sorted([int(x) for x in input().split()])

M = a[(n - 1) // 2]
ans = 0
for i in range(n):
    ans += abs(a[i] - M)

print(M, ans)


# my approach:
# import numpy as np
# n = int(input())
# sequence = sorted(list(map(int, input().split())))
# sequencearr = np.array(sequence)
# middle = int(np.median(sequencearr))
# sum_abs_dev = np.sum(np.abs(sequencearr - middle))


# if n % 2 == 0:
#     median1 = sequence[(n // 2) - 1]
#     median2 = sequence[n // 2]
#     sum1 = np.sum(np.abs(sequencearr - median1))
#     sum2 = np.sum(np.abs(sequencearr - median2))

#     if sum1 == sum2:
#         middle = min(median1, median2)
#     else:
#         middle = median1 if sum1 < sum2 else median2

# print(middle, sum_abs_dev)
