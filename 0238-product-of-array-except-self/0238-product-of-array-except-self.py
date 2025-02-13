class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [1] * n 
        prefix = 1
        for i in range(n):
            result[i] = prefix  # Store the prefix product
            prefix *= nums[i]   # Update prefix product

        # Step 2: Compute suffix products and multiply
        suffix = 1
        for i in range(n - 1, -1, -1):  # Iterate backward
            result[i] *= suffix  # Multiply with suffix product
            suffix *= nums[i]     # Update suffix product

        return result