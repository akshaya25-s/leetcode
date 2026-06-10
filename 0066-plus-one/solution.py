class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=[]
        n=0
        for i in digits:
            n=n*10+i
        n+=1
        l=[int(i) for i in str(n)]
        return l



