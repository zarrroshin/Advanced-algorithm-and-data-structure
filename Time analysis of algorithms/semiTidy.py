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
