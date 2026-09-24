class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s=0
            t=nums[i]
            while t>0:
                u=t%10
                s+=u
                t//=10
            if s==i:
                return i 
        return -1