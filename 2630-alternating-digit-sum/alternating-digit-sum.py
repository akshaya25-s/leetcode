class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=0
        m=str(n)
        for i in range(len(m)):
            if i%2==0:
                s+=int(m[i])
            else:
                s-=int(m[i])
        return s