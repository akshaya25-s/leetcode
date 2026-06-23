class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(0,n+1):
            b=bin(i)
            c=b.count('1')
            l.append(c)
        return l
        
        
        
