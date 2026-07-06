class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        r=0
        c=nums[0]
        for i in range(1,len(nums)):
            r=max(r,(c-1)*(nums[i]-1))
            c=max(c,nums[i])
        return r
