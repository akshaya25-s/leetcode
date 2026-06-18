class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)
        es=(l*(l+1))//2
        s=sum(nums)
        return es-s
        
