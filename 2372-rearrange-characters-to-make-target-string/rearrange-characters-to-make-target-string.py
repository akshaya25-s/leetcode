class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        d=Counter(s)
        t=Counter(target)
        c=float('inf')
        for i in target:
            c=min(d[i]//t[i],c)
        return c
