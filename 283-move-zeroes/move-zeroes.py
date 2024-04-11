class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zeroes = nums.count(0)
        nums[:] = [num for num in nums if num != 0]
        nums.extend([0] * count_zeroes)