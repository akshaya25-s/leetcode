class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        n=len(nums)
        r=[]
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]=2*nums[i]
                nums[i+1]=0
        for i in range(n):
            if  nums[i]!=0:
                r.append(nums[i])
        while len(r)!=n:
            r.append(0)
        
        return r