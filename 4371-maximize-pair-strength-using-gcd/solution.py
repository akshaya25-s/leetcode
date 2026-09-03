class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        m=0
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                n=nums[i]*nums[j]
                g=math.gcd(nums[i],nums[j])   
                m=max(m,n//g**2)
        return m
