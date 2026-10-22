class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hmap={}
        ans=[]
        for x in nums1:
            hmap[x] = hmap.get(x,0)+1
        for x in nums2:
            if x in hmap and hmap[x]>0:
                ans.append(x)
                hmap[x] -= 1
        return ans