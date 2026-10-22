class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        m=bin(n)
        for i in range(len(m)):
            if m[i]=='1':
                c+=1
        return c
