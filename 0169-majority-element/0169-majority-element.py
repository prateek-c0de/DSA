class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
        
        for key in freq:
            if freq[key] > len(nums)//2:
                return key