class Solution:
    def splitNum(self, num: int) -> int:
        a=sorted(str(num))
        n1,n2="",""
        for i in range(len(a)):
            if i%2==0:
                n1+=a[i]
            else:
                n2+=a[i]
        return int(n1)+int(n2)  
                  

        
