class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        s = "".join(ch for ch in s if ch.isalnum()).lower()
        return s == s[::-1]
