class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x):
            l,h=0,len(nums)-1
            while l<=h:
                mid=(l+h)//2
                if nums[mid]<x:
                    l=mid+1
                else:
                    h=mid-1
            return l
        l=search(target)
        h=search(target+1)-1
        if l<=h:
            return [l,h]
        return [-1,-1]

        
