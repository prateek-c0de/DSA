class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dict = {}
        for num in nums:
            dict[num]=dict.get(num,0)+1
        for key in dict:
            if dict[key]>1:
                return True
        return False