class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def sum(n:int)->bool:
            c=0
            for d in str(n):
                if int(d)!=0:
                    if n%(int(d))==0:
                        c+=1
            if c==len(str(n)):
                return True
            else:
                return False
        r=[]
        for i in range(left,right+1):
            if sum(i)==True:
                r.append(i)
        return r
