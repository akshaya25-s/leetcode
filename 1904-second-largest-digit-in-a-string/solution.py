class Solution:
    def secondHighest(self, s: str) -> int:
        se=-1
        fi=None
        num=None
        for i in s:
            if i.isdigit():
                num=int(i)
            if fi==None:
                fi=num
            elif num<fi:
                se=max(se,num)
            elif num>fi:
                temp=fi
                fi=num
                se=temp
        return se
