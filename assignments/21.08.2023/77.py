from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def output(start, com):
            if len(com) == k:
                result.append(com.copy())
                return

            for i in range(start, n + 1):
                com.append(i)
                output(i + 1, com)
                com.pop()

        output(1, [])
        return result