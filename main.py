#
# nums = [1, 2, 1]
#
# a = nums * 2
# print(a)


# nums = [5, 0, 1, 2, 3, 4]
# a = []
# for i in range(len(nums)):
#     if nums[i] not in a:
#         a.append(nums[i])
#     print(a)

address = "1.1.1.1"
a = []
for i, char in enumerate(address):
    if char == '.':
        a.append(i)
    print(i, char)
