class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        def expand_around_center(left, right):
            # Expand outwards and return the longest palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the valid palindrome
            return s[left + 1:right]

        if len(s) == 0:
            return ""

        longest = ""
        for i in range(len(s)):
            # Check for odd-length palindromes (single center)
            odd_palindrome = expand_around_center(i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome

            # Check for even-length palindromes (pair center)
            even_palindrome = expand_around_center(i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest