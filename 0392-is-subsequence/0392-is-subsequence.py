class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        j = 0  # Pointer for sub
        for i in range(len(t)):
            if j < len(s) and t[i] == s[j]:
                j += 1  # Move pointer in sub if match found
        return j == len(s)


        