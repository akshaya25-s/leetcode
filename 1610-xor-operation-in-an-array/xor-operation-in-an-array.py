class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        l=0
        for i in range(n):
            m=start+2*i
            l^=m
        return l
            

