class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=[]
        l=0
        r=sum(nums)
        for num in nums:
            r-=num
            n.append(abs(l-r))
            l+=num
        return n


        
