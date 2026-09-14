class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            if s_dict.get(s[i]):
                s_dict[s[i]] += 1

            else:
                s_dict[s[i]] = 1

            if t_dict.get(t[i]):
                t_dict[t[i]] += 1

            else:
                t_dict[t[i]] = 1
        
        if s_dict == t_dict:
            return True

        return False


        