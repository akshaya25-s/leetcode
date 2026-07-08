class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        d = 0
        for i in num:
            d = d*10+i
        d += k
        res = []
        while d > 0:
            s = d % 10
            res.insert(0,s)
            d = d//10
        return res

        
