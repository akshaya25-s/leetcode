from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r=Counter(nums1)&Counter(nums2)
        return list(r.elements())
