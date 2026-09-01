class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s=sum(nums)
        d=0
        for i in nums:
            while i>0:
                u=i%10
                d+=u
                i//=10
        return s-d
                
