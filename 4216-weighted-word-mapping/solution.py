class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        r=[]
        for i in words:          
            weight = sum(weights[ord(ch) - ord('a')] for ch in i)
            val = weight % 26
            char = chr(ord('z')-val)
            r.append(char)
        
        return "".join(r)

