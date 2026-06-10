class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count=Counter(nums)
        a=0
        for (key,val) in count.items():
            if val==1:
                a+=key
        return a
        
