class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        d=[]
        s=0
        while n>0:
            u=n%10
            d.append(u)
            n//=10
        c=Counter(d)
        for (k,v) in c.items():
            s+=k*v
        return s
        
