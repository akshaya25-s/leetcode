class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m=0
        for s in sentences:
            if len(s.split())>m:
                m=len(s.split())
        return m
