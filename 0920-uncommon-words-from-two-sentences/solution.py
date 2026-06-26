class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter
        s=s1.split()+s2.split()
        d=Counter(s)
        return [key for key,count in d.items() if count==1]




