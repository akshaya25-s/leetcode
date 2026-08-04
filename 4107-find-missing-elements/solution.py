class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        r=[]
        f,l=min(nums),max(nums)
        num=set(nums)
        for i in range(f,l+1):
            if i not in num:
                r.append(i)
        return r 

