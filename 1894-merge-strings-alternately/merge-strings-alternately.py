class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        l=[]
        while i<len(word1) and j<len(word2):
            l.append(word1[i])
            l.append(word2[j])
            i+=1
            j+=1
        if i<len(word1):
            l.append(word1[i:len(word1)])
        elif j <len(word2):
            l.append(word2[i:len(word2)])
        return "".join(l)
                    