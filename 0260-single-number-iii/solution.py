class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c={}
        m=[]
        for n in nums:
            c[n]=c.get(n,0)+1
        for n,c in c.items():
            if c==1:
                m.append(n)
        return m

               
        
