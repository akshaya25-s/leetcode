class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l=[]
        c=Counter(nums)
        for k,v in c.items():
            if v>=2:
                l.append(k)
        return l
