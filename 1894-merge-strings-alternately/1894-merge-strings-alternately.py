class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = "";
        for key,value in enumerate(word1):
            result +=value;
            if(key < len(word2)):
                result += list(word2)[key]  
            if key == len(word1) - 1 and len(word1) < len(word2):
                result += ''.join(list(word2)[key+1:])
        return result

        