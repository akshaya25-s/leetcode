class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = 0
        pg = []
        for i in range(len(nums)):
            n = max(n, nums[i])
            pg.append(math.gcd(nums[i], n))
        pg.sort()
        total_sum = 0
        left = 0
        right = len(pg) - 1
        while left < right:
            total_sum += math.gcd(pg[left], pg[right])
            left += 1
            right -= 1
        return total_sum

