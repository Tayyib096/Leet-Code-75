class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        zeroCount = 0
        maxLen = 0

        while right < len(nums):
            if nums[right] == 0:
                zeroCount+=1
            
            while zeroCount > 1:
                if nums[left] == 0:
                    zeroCount-=1
                left+=1
            maxLen = max(maxLen, right - left)
            right+=1

        return(maxLen)