class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        s=0
        m=sorted(cost)
        m.reverse()
        for i in range(0,len(m)):
            if (i+1)%3!=0:
                s+=m[i]
        return s
            

