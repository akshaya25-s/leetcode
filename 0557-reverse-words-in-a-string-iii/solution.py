class Solution:
    def reverseWords(self, s: str) -> str:
        l=[]
        m=s.split()
        for i in m:
            l.append(i[::-1])
        return " ".join(l)

        
