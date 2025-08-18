#2 задача на leetcode
'''class Solution(object):
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
'''

#3 задача на leetcode
'''class Solution(object):
    def isPalindrome(self, x):
        number_str = str(x)
        reversed_str = number_str[::-1]
        if reversed_str == number_str:
            return True
        else:
            return False
        
x = 121
s = Solution()
s.isPalindrome(x)''' 
