class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
     :rtype: List[bool]
        """
        maxCandies = max(candies)
        result = []
        for index, value in enumerate(candies):
            if value+extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result

        