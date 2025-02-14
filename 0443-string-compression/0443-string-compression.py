class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write_index = 0  # Index to overwrite in the chars array
        read_index = 0   # Index to read from the chars array
        
        while read_index < len(chars):
            char = chars[read_index]  # Get the current character
            count = 0
            
            # Count how many times the current character repeats consecutively
            while read_index < len(chars) and chars[read_index] == char:
                read_index += 1
                count += 1
                
            # Write the character
            chars[write_index] = char
            write_index += 1
            
            # If the character repeats more than once, write the count
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1
        
        return write_index 