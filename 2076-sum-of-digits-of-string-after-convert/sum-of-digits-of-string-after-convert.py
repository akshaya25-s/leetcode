class Solution:
    def getLucky(self, s: str, k: int) -> int:
        al='abcdefghijklmnopqrstuvwxyz'
        l=[]
        for st in s:
            l.append(al.find(st)+1)
        n = "".join(str(x) for x in l)
        m=int(n)
        for i in range(k):
            su=0
            while m>0:
                su+=m%10
                m//=10
            m=su
        return m
        


