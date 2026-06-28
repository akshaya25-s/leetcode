class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        for d in range(len(s)):
            left = s[d:] + s[:d]
            if left==goal:
                return True
        return False


