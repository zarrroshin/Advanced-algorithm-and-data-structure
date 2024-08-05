import sys

n = int(input())
nums = list(map(int, input().split()))

maximumSubArraySum = -sys.maxsize-1
start = 0
end = 0

for left in range(n):
    runningWindowSum = 0
    for right in range(left, n):
        runningWindowSum += nums[right]
        if runningWindowSum > maximumSubArraySum:
            maximumSubArraySum = runningWindowSum
            start = left
            end = right
print(maximumSubArraySum)
