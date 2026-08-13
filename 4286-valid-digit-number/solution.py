class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        l=str(n)
        if str(x) in l and l[0]!=str(x):
                return True
        else:
            return False
