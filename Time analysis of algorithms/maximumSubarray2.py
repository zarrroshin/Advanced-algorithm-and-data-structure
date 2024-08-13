n = int(input())
nums = list(map(int, input().split()))

start = 0
end = 0

maxSoFar = nums[0]
maxEndingHere = nums[0]

for i in range(1, n):
    maxEndingHere += nums[i]
    if nums[i] > maxEndingHere:
        maxEndingHere = nums[i]
        if maxSoFar < maxEndingHere:
            start = i
    if maxSoFar < maxEndingHere:
        maxSoFar = maxEndingHere
        end = i
print(maxSoFar)
