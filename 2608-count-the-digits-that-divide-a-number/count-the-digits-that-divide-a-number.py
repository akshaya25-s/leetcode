class Solution:
    def countDigits(self, num: int) -> int:
        m=0
        n=num
        while n>0:
            u=n%10
            n//=10
            if num%u==0:
                m+=1
        return m
            
