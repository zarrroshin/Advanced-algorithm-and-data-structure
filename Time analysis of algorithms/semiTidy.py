# this is a good algorithm if we have any kind of sequence (decreasing or increasing)

n = int(input())
nums = list(map(int, input().split()))


if nums == sorted(nums):
    print("NO")
    exit()

first_decreasing = -1
for i in range(n - 1):
    if nums[i] > nums[i + 1]:
        first_decreasing = i
        break

last_decreasing = -1
for i in range(n - 1, 0, -1):
    if nums[i] < nums[i - 1]:
        last_decreasing = i
        break

nums[first_decreasing], nums[last_decreasing] = nums[last_decreasing], nums[first_decreasing]

if nums == sorted(nums):
    print("YES")
else:
    print("NO")

# if we are sure that sequence is permutation to length n contains numbers 1 to n it would be easier

n = int(input())
a = list(map(int, input().split()))
# count bad numbers
count = 0
for i in range(n):
    if a[i] - 1 != i:
        count = count + 1

if count == 2:
    print('YES')
else:
    print('NO')
