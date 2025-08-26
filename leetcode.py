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
'''class Solution(object):
    def romanToInt(self, s):
        values = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000,
            "IV": 4, "IX": 9,
            "XL": 40, "XC": 90,
            "CD": 400, "CM": 900
        }
        
        i = 0
        number = 0
        while i < len(s):
            # пробуем взять два символа
            if i + 1 < len(s) and s[i:i+2] in values:
                number += values[s[i:i+2]]
                i += 2
            else:
                number += values[s[i]]
                i += 1
        return number'''

