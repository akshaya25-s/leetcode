class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        l=set()
        u=set()
        for ch in word:
            if ch.islower():
                l.add(ch)
            else:
                u.add(ch.lower())
        sc=0
        for ch in l:
            if ch in u:
                sc+=1
        return sc
