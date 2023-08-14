class Solution(object):
    def reverseString(self, s, index=0):
        if index >= len(s) // 2:
            return 
        s[index], s[len(s) - 1 - index] = s[len(s) - 1 - index], s[index]
        self.reverseString(s, index + 1)