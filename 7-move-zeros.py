class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        for index in range(len(nums)):
            if nums[index]!= 0:
                nums[index], nums[l]= nums[l], nums[index]
                l += 1
                    
        return (nums)