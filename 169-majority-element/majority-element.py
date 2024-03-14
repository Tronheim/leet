class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = nums[0], 1
        
        for num in nums[1:]:
            if count == 0:
                candidate, count = num, 1
            elif candidate == num:
                count += 1
            else:
                count -= 1
        
        return candidate