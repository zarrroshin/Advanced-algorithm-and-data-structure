# solution
n, q = map(int, input().split())
a = list(map(int, input().split()))

for i in range(q):
    t = int(input())
    ans = 0
    for x in a:  # calculating number of sad people in n opeartions
        if t > x:
            ans += 1
    print(ans)

# total number of operations is n * q


# my approach:
# string = input().split(" ")
# n = int(string[0])
# q = int(string[1])
# nums = input().split(" ")
# questions =[]
# for i in range(q):
#     questions.append(int(input()))
# for i in range(q):
#     count =0
#     for j in range(len(nums)):
#         if int(nums[j])<questions[i]:
#             count+=1
#     print(count)
