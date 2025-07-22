class Solution:
    def increasingTriplet(self, nums) -> bool:
        first = float('inf')
        second = float('inf')
        for i in nums:
            if i<=first:
                first = i
            elif i<=second:
                second = i
            else:
                return (True)
        return (False)