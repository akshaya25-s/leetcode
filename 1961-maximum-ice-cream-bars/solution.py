class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        s,c=0,0
        for i in costs:
            s+=i
            if s<=coins:
                c+=1
            else:
                break
        return c
            


        
