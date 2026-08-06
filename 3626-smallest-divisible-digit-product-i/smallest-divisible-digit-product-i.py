class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            p=1
            i=n
            while i>1:
                u=i%10
                p*=u
                i//=10
            if p%t==0:
                return n
            n+=1


            
