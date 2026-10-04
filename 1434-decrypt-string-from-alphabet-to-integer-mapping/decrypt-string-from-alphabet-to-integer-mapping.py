class Solution:
    def freqAlphabets(self, s: str) -> str:
        m='abcdefghijklmnopqrstuvwxyz'
        l=[]
        i=len(s)-1
        while i >= 0:
            if s[i] == '#':
                n = s[i-2:i] 
                l.append(m[int(n) - 1])
                i -= 3
            else:
                l.append(m[int(s[i]) - 1])
                i -= 1
        return "".join(reversed(l))