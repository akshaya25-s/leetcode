class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        for w in words:
            w_lower = set(w.lower())
            
            if w_lower <= row1 or w_lower <= row2 or w_lower <= row3:
                result.append(w)
                
        return result

