class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mi=min(nums)
        ma=max(nums)
        return gcd(mi,ma)
