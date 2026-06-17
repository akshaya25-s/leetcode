class Solution:
    def calPoints(self, operations: List[str]) -> int:
        r=[]
        for i in operations:
            if i=='+':
                r.append(r[-1]+r[-2])
            elif i=="C":
                r.pop()
            elif i=='D':
                r.append(r[-1]*2)
            else:
                r.append(int(i))
        return sum(r)
        
