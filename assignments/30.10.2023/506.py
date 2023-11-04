class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort = sorted(score, reverse=True)
        ranks = ["Gold Medal","Silver Medal","Bronze Medal"]+list(map(str,range(4,len(score)+1)))
        dic = {score:rank for score, rank in zip(sort,ranks)}
        return [dic[s] for s in score]