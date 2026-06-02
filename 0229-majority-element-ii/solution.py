class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c={}
        m=[]
        for n in nums:
            c[n]=c.get(n,0)+1
        for n,c in c.items():
            if c>len(nums)//3:
                m.append(n)
        return m
            


