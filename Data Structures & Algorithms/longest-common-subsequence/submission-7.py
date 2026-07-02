class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        nexta = [0 for _ in range(n+1)]
        curr = [0 for _ in range(n+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    curr[j] = 1 + nexta[j+1]
                else:
                    curr[j] = max(nexta[j], curr[j+1])
            nexta = curr.copy()
        # print(dp)
        return curr[0]
        