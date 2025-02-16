class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seq = s[:10]
        
        sett = set()
        result = {}
        
        for start in range(len(s) - 9):
            seq = s[start : start + 10]
            if seq in sett and seq not in result:
                result[seq[:]] = 1
            sett.add(seq)
        return result.keys()

        # Convert the repeated set to a list and return
        return list(repeated)
        