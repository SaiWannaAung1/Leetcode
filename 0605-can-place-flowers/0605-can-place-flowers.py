class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        inc = 0 if len(flowerbed) == 1 else 1
        for index, value in enumerate(flowerbed):
            if (value == 0):
                if (index == 0 and flowerbed[index + inc] == 0):
                    flowerbed[index] = 1
                    count += 1
                elif (index == len(flowerbed) - inc and flowerbed[index - inc] == 0):
                    flowerbed[index] = 1
                    count += 1
                elif 0 < index < len(flowerbed) - 1 and flowerbed[index + inc] == 0 and flowerbed[index - inc] == 0:
                    flowerbed[index] = 1
                    count += 1
        return count >= n

            
            
        