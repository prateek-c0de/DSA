class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        prefix_counts = {0: 1}
        odd_count = 0
        res = 0
        
        for num in nums:
            odd_count += num % 2
            res += prefix_counts.get(odd_count - k, 0)
            prefix_counts[odd_count] = prefix_counts.get(odd_count, 0) + 1
            
        return res