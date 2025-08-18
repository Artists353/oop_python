class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  # словарь: число -> индекс
        for index, value in enumerate(nums):
            difference = target - value
            if difference in seen:  # нашли пару
                return [seen[difference], index]
            seen[value] = index
        return []  # если не нашли
        

nums = [2, 7, 11, 15]
target = 9
s = Solution()
print(s.twoSum(nums, target))
