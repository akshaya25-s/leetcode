class Solution:
    def reverseDegree(self, s: str) -> int:
        m='abcdefghijklmnopqrstuvwxyz'
        c=0
        for i,j in enumerate(s):
            ra=26-m.find(j)
            p=(i+1)*ra
            c+=p
        return c