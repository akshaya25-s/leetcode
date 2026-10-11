class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        t=0
        n=len(arr)
        for i ,j in enumerate(arr):
            ts=(i+1)*(n-i)
            c=(ts+1)//2
            t+=j*c
        return t
