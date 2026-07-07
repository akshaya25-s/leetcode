class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=0
        m=""
        if n==0:
            return 0
        while n>0:
            u=n%10
            s+=u
            if u!=0:
                m+=str(u)
            n//=10
        if m=="":
            return 0
        return int(m[::-1])*s
    
         



