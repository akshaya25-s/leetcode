class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            t=num
            s=0
            while t>0:
                d=t%10
                s+=d
                t//=10
            num=s
        return num


            
