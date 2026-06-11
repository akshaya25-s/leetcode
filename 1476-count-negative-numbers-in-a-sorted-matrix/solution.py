class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        from collections import Counter
        c=[Counter(j<0 for j in i )[True] for i in grid]
        return sum(c)



        
