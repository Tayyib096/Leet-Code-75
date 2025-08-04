class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max_a = 0
        curr_a = 0
        for g in gain:
            curr_a += g
            max_a = max(max_a, curr_a)
        return(max_a)