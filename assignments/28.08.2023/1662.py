class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1=""
        str2=""
        for i in range(0,len(word1)):
            str1=str1+word1[i]
        for j in range(0,len(word2)):
            str2=str2+word2[j]
        if len(str1)==len(str2):
            if str1==str2:
                return 1
            else:
                return 0
        else:
            return 0