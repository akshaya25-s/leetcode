class Solution:
    def maxDepth(self, s: str) -> int:
        c=0
        maxc=0
        stack=[]
        for i in s:
            if i=='(':
                stack.append(i)
                c+=1
            elif i==')':
                if c>maxc:
                    maxc=c
                c-=1
                stack.pop()
        return maxc

        
