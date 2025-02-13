class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        my_list = list(s)
        targets = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        found_items = [(index, value) for index, value in enumerate(my_list) if value.lower() in targets]
        vowels = [value for _, value in found_items]
        vowels.reverse()
        result_list = my_list[:]
        vowel_index = 0
        for index, _ in found_items:
            result_list[index] = vowels[vowel_index]
            vowel_index += 1
        
        return ''.join(result_list)



        