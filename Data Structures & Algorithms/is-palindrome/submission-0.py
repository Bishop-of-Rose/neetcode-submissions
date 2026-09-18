class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.is_alnum(s[l]):
                l += 1 
            while l < r and not self.is_alnum(s[r]):
                r -= 1
            print(s[l], s[r])
            if s[l].lower() != s[r].lower():
                return False 

            l, r = l + 1, r - 1
        return True

    def is_alnum(self, c) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
        