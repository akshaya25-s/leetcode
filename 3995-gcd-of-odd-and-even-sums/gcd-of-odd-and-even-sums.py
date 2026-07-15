class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        import math
        e=n*(n+1)
        o=n*n
        return math.gcd(o,e)