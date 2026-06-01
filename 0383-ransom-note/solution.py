class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r=list(ransomNote)
        m=list(magazine)
        result=[]
        for ch in ransomNote:
            if ch in m:
                m.remove(ch)
                result.append(ch)
        if len(result)==len(ransomNote):
            return True
        else:
            return False
