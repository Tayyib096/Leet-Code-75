class Solution:
    def reverseVowels(self, s: str) -> str:
        sLst = list(s)
        l = 0
        r = len(sLst)-1

        vowels = ['a','e','i','o','u']

        while l < r:
            if (sLst[l]).lower() not in vowels:
                l+=1
            
            if (sLst[r]).lower() not in vowels:
                r-=1

            if (sLst[l]).lower() in vowels and (sLst[r]).lower() in vowels:
                # Parallel Swapping Prevents the variable from being re-assigned before swapping 
                sLst[l], sLst[r] = sLst[r], sLst[l]
                l+=1
                r-=1

        return (''.join(sLst))