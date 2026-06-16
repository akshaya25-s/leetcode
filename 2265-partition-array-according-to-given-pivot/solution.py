class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l=[]
        r=[]
        e=[]
        for num in nums:
            if num==pivot:
                e.append(num)
            elif num<pivot:
                l.append(num)
            else:
                r.append(num)
        return l+e+r
