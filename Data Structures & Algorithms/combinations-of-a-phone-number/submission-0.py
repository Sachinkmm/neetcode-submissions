class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapp = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                ans.append(curStr)
                return
            for c in mapp[int(digits[i])]:
                backtrack(i+1, curStr + c)
        
        if digits:
            backtrack(0, "")
        return ans

        