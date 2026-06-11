class Solution:
    def isPalindrome(self, s: str) -> bool:
        c="".join(i.lower() for i in s if i.isalnum())
        return c==c[::-1]
        
