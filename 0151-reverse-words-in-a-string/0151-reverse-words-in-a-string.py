class Solution(object):
    def reverseWords(self, s):
        scentence = s.split(" ")
        filtered_list = [word for word in scentence if word]
        return ' '.join(filtered_list[::-1])

        
        