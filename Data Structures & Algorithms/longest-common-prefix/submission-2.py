class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]
        for s in strs:
            if longest == "":
                break

            if longest.startswith(s):
                longest = s

            for i in range(len(longest)):
                if longest[i] != s[i]:
                    longest = s[:i]
                    break

        return longest

                

        