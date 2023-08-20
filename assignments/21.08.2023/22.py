class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def rec(left,right,stack,can):
            if left==0 and right==0:
                result.append(can)
                return

            if left>0:
                rec(left-1,right,stack+1,can+"(")
            if right>0 and stack>0:
                rec(left,right-1,stack-1,can+")")
        rec(n,n,0,"")
        return result