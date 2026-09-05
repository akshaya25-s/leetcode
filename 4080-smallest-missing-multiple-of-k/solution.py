class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s=set(nums)
        n=1
        while n!=0:
            m=k*n
            if m not in s:
                return m
            n+=1
