class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        oringal = list(enumerate(nums))  # [(index, value)]
        oringal.sort(key=lambda x: x[1])  # Sort by value


        left, right = 0, len(nums)-1
        while (left < right):
            sum_value = oringal[left][1] + oringal[right][1]
            if sum_value == target:
                print(nums)
                print(oringal)
                result.append(oringal[left][0])
                result.append(oringal[right][0])
                return result
            elif sum_value < target:
                left +=1
            else:
                right -=1
        return False               
        