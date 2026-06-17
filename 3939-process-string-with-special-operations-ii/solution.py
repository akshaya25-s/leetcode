class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        length = [0] * (n + 1)
        for i, ch in enumerate(s):
            cur = length[i]
            if ch.isalpha():
                length[i + 1] = cur + 1
            elif ch == '*':
                length[i + 1] = max(0, cur - 1)
            elif ch == '#':
                length[i + 1] = cur * 2
            elif ch == '%':
                length[i + 1] = cur
        if k >= length[n]:
            return '.'
        for i in range(n - 1, -1, -1):
            ch = s[i]
            if ch.isalpha():
                if k == length[i]:
                    return ch
            elif ch == '*':
                if length[i] > 0:
                    k = min(k, length[i] - 1)
            elif ch == '#':
                if k >= length[i]:
                    k -= length[i]
            elif ch == '%':
                k = length[i] - 1 - k
        return '.'
        
