class Solution:
    def maxOperations(self, nums, k: int) -> int:

        n_dict = dict()
        ans = 0

        for i, n in enumerate(nums):
            complement = k - n
            if n_dict[complement] > 0:
                ans += 1
                n_dict[complement] -= 1
            else:
                n_dict[n] += 1
        return ans