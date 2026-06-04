class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        r=[]
        s=0
        for i in nums:
            s+=i
            r.append(s)
        return(r)
       
