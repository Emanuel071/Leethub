# Code adapted from Sahil Sharma, used with permission, from Spring, 2021
from math import pow
from math import log2
from math import factorial


#NOTE: Brute Force O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output_list = []
        # first_index = 0
        # first_pass = True
        for index_1 in range(len(nums)):
            for index_2 in range(index_1+1, len(nums)):
                if nums[index_1] + nums[index_2] == target:
                    output_list.append(index_1)
                    output_list.append(index_2)            
        return output_list

#NOTE:  O(n)
class Faster_Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        answer = []

        for i in range(len(nums)):
            secondNumber = target-nums[i]
            if(secondNumber in dictionary.keys()):
                secondIndex = nums.index(secondNumber)
                if(i != secondIndex):
                    return sorted([i, secondIndex])     
            dictionary.update({nums[i]: i})      

# nums = [2,7,11,15]
# target = 9
nums = [3,2,4]
target = 6
# nums = [3,3]
# target = 6
solution = []

print(Faster_Solution.twoSum(solution,nums, target))

# more info:
# https://medium.com/@snehakweera77/1-two-sum-5421e63ce7f3
