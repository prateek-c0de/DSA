class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dict = Counter(nums)
        for key in dict:
            if dict[key] > len(nums)//2:
                return key