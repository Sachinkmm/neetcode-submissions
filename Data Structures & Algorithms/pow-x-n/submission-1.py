class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        N = abs(n)
        while N > 0:
            if N & 1:
                ans *= x
            x *= x
            N >>= 1
        return ans if n >= 0 else 1 / ans