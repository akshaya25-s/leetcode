class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=0
        for i in range(0,len(nums)):
            n=max(n,nums[i])
            m=nums[i]
            for j in range(i,len(nums)):
                m=min(m,nums[j])
            if n-m<=k:
                return i
        return -1

