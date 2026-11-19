class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        hmap = {0:1}
        prefix =0
        count =0 
        for i in nums:
            prefix += i
            rem = prefix % k

            if rem in hmap:
                count += hmap[rem]
                hmap[rem] += 1
            else:
                hmap[rem] = 1
        return count