class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # count = 0
        # inc = 0 if len(flowerbed) == 1 else 1
        # for index, value in enumerate(flowerbed):
        #     if (value == 0):
        #         if (index == 0 and flowerbed[index + inc] == 0):
        #             flowerbed[index] = 1
        #             count += 1
        #         elif (index == len(flowerbed) - inc and flowerbed[index - inc] == 0):
        #             flowerbed[index] = 1
        #             count += 1
        #         elif 0 < index < len(flowerbed) - 1 and flowerbed[index + inc] == 0 and flowerbed[index - inc] == 0:
        #             flowerbed[index] = 1
        #             count += 1
        # return count >= n
        planted = 0
        # Indicates the number of flowers that have been successfully planted
        for i in range (len(flowerbed)):
            if flowerbed[i] == 0:
                # if(flowerbed[i-1] == 0) and (flowerbed[i+1] == 0):
                    # The first and last elements are not handled correctly. In particular, when the current position is the first or last element of the flowerbed, accessing flowerbed[i-1] or flowerbed[i+1] will result in an out-of-bounds error.
                    if(i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                    # When checking the current flowerbed[i] == 0, if it is the first element (i == 0), there is no need to check the left side; if it is the last element (i == len(flowerbed)-1), there is no need to check the right side.
                        flowerbed[i] = 1
                        planted += 1
            if planted >= n:
                return True
        return False 


            
            
        