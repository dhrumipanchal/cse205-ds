class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result=""
        for o in order:
            for j in range(len(s)):
                if s[j]==o:
                    result+=s[j]
            s = s.replace(o,'')
        result+=s
        return result