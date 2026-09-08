class Solution:
    def removeZeros(self, n: int) -> int:
        m=str(n)
        s=m.replace('0','')
        return int(s)