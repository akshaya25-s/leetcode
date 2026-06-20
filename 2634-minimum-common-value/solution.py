class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s=set(nums2)
        r=[]
        for i in nums1:
             if i in s:
                 r.append(i)
        if r:        
             return min(r)
        else:
             return -1

