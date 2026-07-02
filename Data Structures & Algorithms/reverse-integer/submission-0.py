class Solution:
    def reverse(self, x: int) -> int:
        n = abs(x)
        ans = 0
        while n > 0:
            ans = ans * 10 + (n % 10)
            n = n // 10
        if x < -1e9+7 or x > 1e9+7:
            return 0
        if x < 0:
            return -ans
        return ans