class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n, ans, inc, dec=len(nums), 1, 1, 1
        for i in range(1, n):
            A=nums[i]>nums[i-1]
            B=nums[i]<nums[i-1]
            inc=A*inc+1
            dec=B*dec+1
            ans=max(ans, dec, inc)
        return ans