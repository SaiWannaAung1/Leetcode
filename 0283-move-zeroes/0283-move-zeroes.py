class Solution(object):
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(0)
        return nums
        