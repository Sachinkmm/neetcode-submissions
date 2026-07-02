class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            val = 0
            while n > 0:
                val += (n % 10)**2
                n = n // 10
            if val == 1:
                return True
            if val in seen:
                return False
            seen.add(val)
            n = val
        return False