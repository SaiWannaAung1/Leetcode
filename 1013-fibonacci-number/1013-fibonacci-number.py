class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 0):
            return 0

        # Stop condition
        if (n == 1 or n == 2):
            return 1
        else:
            return (self.fib(n-1) + self.fib(n-2))
        