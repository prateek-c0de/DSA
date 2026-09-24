class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]^nums[i-1] ==0:
                return nums[i]