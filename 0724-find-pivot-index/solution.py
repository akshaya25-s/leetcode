class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t=sum(nums)
        l=0
        r=0
        for i,num in enumerate(nums):
            r=t-l-num
            if l==r:
                return i
            l+=num
        return -1        
