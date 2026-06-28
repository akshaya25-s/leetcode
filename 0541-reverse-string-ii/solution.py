class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        r = [s[i:i+k] for i in range(0, len(s), k)]
        m=[r[j][::-1] if j%2==0 else r[j] for j in range(len(r))]
        return "".join(m)


