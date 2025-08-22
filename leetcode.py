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

#4 задача на leetcode
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        # взять первую строку как базовую
        prefix = strs[0]
        for s in strs[1:]:
            # сокращаем prefix пока он не является префиксом s
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

s = Solution()
strs = ["flower","flow","flight"]
print(s.longestCommonPrefix(strs))  # -> "fl"

