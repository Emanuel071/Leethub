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
            if value == target:
                output_list.append(target)
            else:
                continue
            starter_integer = integer
        return output_list

        