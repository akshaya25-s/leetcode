class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        a=0
        for num in nums:
            if len(str(num))%2==0:
                a+=1
        return a
