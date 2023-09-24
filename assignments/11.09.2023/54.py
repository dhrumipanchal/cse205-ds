class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        while matrix:
            result += matrix[0]
            matrix.pop(0)

            if not matrix:
                break

            matrix = list(zip(*matrix))[::-1]

        return result
