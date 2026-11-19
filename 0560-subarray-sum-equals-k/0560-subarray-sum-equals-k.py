class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        heap={0:1}
        prefix=0
        ans=0
        for i in range(len(nums)):
            prefix +=nums[i]
            diff=prefix-k
            if diff in heap:
                ans+=heap[diff]
            heap[prefix]= 1+heap.get(prefix,0)
        return ans