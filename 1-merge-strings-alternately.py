class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''

        if(len(word1) == len(word2)):
            for i in range(len(word1)):
                res += word1[i]+word2[i]

        if(len(word1) > len(word2)):
            shortWord = word1[:len(word2)]
            remaining = word1[len(word2):]
            for i in range(len(word2)):
                res += shortWord[i] + word2[i]
            res += remaining

        if(len(word1) < len(word2)):
            shortWord = word2[:len(word1)]
            remaining = word2[len(word1):]
            for i in range(len(word1)):
                res += word1[i] + shortWord[i]
            res += remaining


        return(res)