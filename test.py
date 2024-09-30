# # 1 
# price=[7,6,4,3,1]

# def calculate_distance(prices):
#     max_profit = 0
#     buy_price = prices[0]
#     for price in prices:
#         if buy_price > price:
#             buy_price = price
#         elif max_profit < price - buy_price:
#             max_profit = price - buy_price

#     return max_profit
# print(calculate_distance(price))


# 2
# nums = [2,2,1,1,1,2,2]
# print(max(set(nums),key=nums.count))


# 3

# def removeDuplicates(nums: list[int]) -> int:
#     j = 0
#     for i in range(1,len(nums)):
#         if nums[i] != nums[j]:
#             j += 1
#             nums[j] = nums[i]
#     return nums

# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

# 4

# def removeElement(nums: list[int], val: int) -> int:
#     index = 0
#     for i in range(len(nums)):
#         if nums[i] != val:
#             nums[index] = nums[i]
#             index += 1
#     return index,nums

# print(removeElement([0,1,2,2,3,0,4,2], 2))

# 5

# from collections import Counter
# def canConstruct(ransomNote: str, magazine: str) -> bool:
#     c1 = Counter(ransomNote)
#     c2 = Counter(magazine)
#     return c1 == c1 & c2

# canConstruct('aaab','baaab')


# 6

# def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#     """
#     Do not return anything, modify nums1 in-place instead.
#     """
#     index_m = m - 1
#     index_n = n - 1 
#     index_writh = n + m -1

#     while index_n>=0:
#         if index_m >= 0 and nums1[index_m] > nums2[index_n]:
#             nums1[index_writh] = nums1[index_m]
#             index_m -= 1
#         else:
#             nums1[index_writh] = nums2[index_n]
#             index_n -= 1
#         index_writh -= 1

# merge([1,2,3,0,0,0],3,[2,5,6],3)

# 7
# ------------------------------------------------------------------------------
# import turtle

# for steps in range(50):
#     for c in ('blue', 'red', 'green'):
#         turtle.color(c)
#         turtle.fd(steps)
#         turtle.right(30)
#         turtle.speed(0)
# ------------------------------------------------------------------------------

s = "   fly me   to   the moon  "
# text = s.split()
# print(len(text[-1]))

l = 0
i = len(s)
while i>0:
    i-=1
    if s[i]!=" ":
        l+=1
    elif l != 0:
        break

print(l)