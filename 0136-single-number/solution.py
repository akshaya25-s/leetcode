class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c={}
        for key in nums:
            if key in c:
                c[key]+=1
            else:
                c[key]=1
        return min(c,key=c.get)



        
