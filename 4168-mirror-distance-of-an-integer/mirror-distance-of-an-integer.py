class Solution:
    def mirrorDistance(self, n: int) -> int:
        m=str(n)
        r=abs(n-int(m[::-1]))
        return r