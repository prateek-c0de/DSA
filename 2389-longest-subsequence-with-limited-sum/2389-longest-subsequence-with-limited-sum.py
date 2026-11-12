class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        res = []
        n =len(nums)
        for i in range(1,n):
            nums[i]+=nums[i-1]
        for q in queries:
            left=0
            right=n-1
            total=-1
            while left<=right:
                mid=left+(right-left)//2
                if nums[mid]<=q:
                    total=mid
                    left=mid+1
                else:
                    right=mid-1
            res.append(total+1 if total!=-1 else 0)
        return res