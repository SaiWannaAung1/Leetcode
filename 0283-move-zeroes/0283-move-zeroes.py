class Solution(object):
    def moveZeroes(self, nums):
        z=0
        p=0
        for i in nums:
            if (i==0):
                z+=1
            else:
                nums[p]=i
                p+=1
        if z>0:   
            nums[-z:]=[0]*z
        return nums
        