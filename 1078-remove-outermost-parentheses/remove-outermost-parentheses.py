class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st=[]
        d=0
        for i in range(len(s)):
            if s[i]=='(':
                if d>0:
                    st.append(s[i])
                d+=1          
            else:
                d-=1
                if d>0:
                    st.append(s[i])
        return "".join(st)

            

