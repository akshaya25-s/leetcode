class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        m=float("inf")
        l=0
        s=0
        for r in range(len(nums)):
            s+=nums[r]
            while s>=target:
                if r-l+1<m:
                    m=r-l+1
                s-=nums[l]
                l+=1
        return m if m!=float("inf") else 0
