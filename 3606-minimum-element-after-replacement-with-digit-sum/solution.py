class Solution:
    def minElement(self, nums: List[int]) -> int:
        m=[]
        for n in nums:
            t=n
            sum=0
            while t>0:
                
                d=t%10
                sum+=d
                t//=10
            m.append(sum)
        return min(m)
            

