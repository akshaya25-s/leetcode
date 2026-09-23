class Solution:
    def countEven(self, num: int) -> int:
        l=[]
        for i in range(1,num+1):
            s=0
            t=i
            while i>0:
                u=i%10
                s+=u
                i//=10
            if s%2==0:
                l.append(t)
        return len(l)
