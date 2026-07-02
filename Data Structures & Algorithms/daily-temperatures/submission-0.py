class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []
        ans = [0] * n
        for i in range(n):
            while st and temperatures[st[-1]] < temperatures[i]:
                ans[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)
        return ans
        