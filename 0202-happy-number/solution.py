class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  
        while n != 1 and n not in seen:
            seen.add(n)
            t = n
            s = 0
            while t > 0: 
                d = t % 10
                s += d ** 2
                t //= 10
            n = s  
        return n == 1
