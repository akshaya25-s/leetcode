class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        al=set(allowed)
        c=0
        for w in words:
            if all(ch in al for ch in w):
                c+=1
        return c
