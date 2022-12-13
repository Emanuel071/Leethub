class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output_list = []
        starter_integer = 0
        for integer in nums:
            value = starter_integer + integer
            # print("starter: " + str(starter_integer))
            # print("integer: " + str(integer))
            # print("value: " + str(value))
            # print("")
            if value == target and starter_integer != 0:
                output_list.append(nums.index(starter_integer))
                output_list.append(nums.index(integer))
                starter_integer = integer
            else:
                starter_integer = integer
                continue
        return output_list

nums = [2,7,11,15]
target = 9
solution = []

print(Solution.twoSum(solution,nums, target))