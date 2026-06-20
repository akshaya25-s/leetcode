class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m=sorted(nums)
        l=m[-1]
        r=[]
        for i in range(1,l):
            r.append(i)
        r.append(l)
        r.append(l)
        return r==m
