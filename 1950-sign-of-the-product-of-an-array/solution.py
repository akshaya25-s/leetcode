class Solution:
    def arraySign(self, nums: List[int]) -> int:
        s=1
        for num in nums:
            if num==0:
                return 0
            elif num>0:
                continue
            else:
                s=-1*s
        return s
