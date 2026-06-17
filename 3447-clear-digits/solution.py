class Solution:
    def clearDigits(self, s: str) -> str:
        r=[]
        for i in s:
            if i.isdigit():
                r.pop()
            else:
                r.append(i)
        return "".join(r)



