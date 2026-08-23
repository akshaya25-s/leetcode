class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original=n
        d=0
        p=1
        while n>0:
            u=n%10
            d+=u
            p*=u
            n//=10
        return original%(d + p)  == 0


