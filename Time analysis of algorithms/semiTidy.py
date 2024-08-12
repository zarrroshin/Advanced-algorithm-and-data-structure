n = int(input())
nums = list(map(int, input().split()))

count = 0
maximum = max(nums)
max_index = nums.index(maximum)
if (nums[len(nums)-1] != maximum):
    nums[len(nums)-1], nums[max_index] = maximum, nums[len(nums)-1]
    count += 1
nums.remove(maximum)
nums1 = sorted(nums)
if (nums == nums1):
    print("YES")
    exit()
else:
    print("NO")
    exit()
