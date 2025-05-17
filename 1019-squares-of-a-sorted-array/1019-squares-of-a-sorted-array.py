class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list2 = []
        left , right = 0, len(nums)-1
        while left <= right:
            if abs(nums[left]) >  abs(nums[right]):
                list2.append(nums[left] **2)
                left += 1  # Move left pointer to the right
            else:
                list2.append(nums[right] ** 2)
                right -= 1  # Move right pointer to the left
        list2.reverse()
        return list2
        