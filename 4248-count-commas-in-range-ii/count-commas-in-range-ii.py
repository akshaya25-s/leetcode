class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        length = len(str(n))  
        for i in range(4, length + 1):
            commas = (i - 1) // 3
            start = 10 ** (i - 1)
            end = min(n, 10 ** i - 1)
            total += (end - start + 1) * commas  
        return total
