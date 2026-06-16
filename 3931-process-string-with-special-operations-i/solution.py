class Solution:
    def processStr(self, s: str) -> str:
        r=[]
        for i in s:
            if i.isalpha():
                r.append(i)
            elif i=='*':
                if r:
                    r.pop()
            elif i=='#':
                r.extend(r)
            elif i=='%':
                r=r[::-1]
        return "".join(r)


