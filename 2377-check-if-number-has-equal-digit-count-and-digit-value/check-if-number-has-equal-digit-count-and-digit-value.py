class Solution:
    def digitCount(self, num: str) -> bool:
        from collections import Counter
        c=Counter(num)
        for i,j in enumerate(num):
            if int(j)!=c[str(i)]:
                return False
        return True