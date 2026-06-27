class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        s=0
        for i in range(k):
            s+=nums[i]
        m=s/k
        for i in range(k,n):
            s+=nums[i]-nums[i-k]
            a=s/k
            m=max(a,m)
        return m
