class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        c=0
        d=Counter(chars)
        for i in words:
            w=Counter(i)
            if all(w[j] <= d[j] for j in w):
                c+=len(i)
        return c


