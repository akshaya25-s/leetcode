class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st=[0]
        for i in s:
            if i=='(':
                st.append(0)
            else:
                m=st.pop()
                st[-1]+=max(2*m,1)
        return st[0]

