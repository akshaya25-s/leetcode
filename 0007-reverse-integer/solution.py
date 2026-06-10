class Solution:
    def reverse(self, x: int) -> int:
        if x<-2**31 or x>2**31-1:
            return 0
        s=-1 if x<0 else 1
        n=str(abs(x))
        r=n[::-1]
        a=s*int(r)
        if a<-2**31 or a>2**31-1:
            return 0
        return a
        
