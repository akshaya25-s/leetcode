class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        t=x
        s=0
        while t>0:
            d=t%10
            s+=d
            t//=10
        if x%s==0:
            return s
        else:
            return -1
