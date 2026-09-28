class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        m=max(candies)
        r=[]
        for i in candies:
            r.append(i+extraCandies>=m)
        return r
            
            