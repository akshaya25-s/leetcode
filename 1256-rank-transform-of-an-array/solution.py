class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s=sorted(set(arr))
        r={val:i+1 for i,val in enumerate(s)}
        l=[]
        for j in arr:
            l.append(r[j])
        return l
        
