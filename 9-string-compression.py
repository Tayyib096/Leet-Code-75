class Solution:
    def compress(self, chars) -> int:
        i = 0
        counter = 1

        for j in range(1,len(chars) + 1):
            if j < len(chars) and chars[j] == chars[j-1]:
                counter += 1  # Increment the counter for the current group
            else:
                chars[i] = chars[j-1]  # Store the character in the modified chars array
                i += 1

            if counter > 1:
                for digit in str(counter):
                    chars[i] = digit  # Store each digit of the counter in the modified chars array
                    i += 1

            counter = 1  # Reset the counter for the next group
        return(i)