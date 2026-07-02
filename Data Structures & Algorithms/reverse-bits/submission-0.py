class Solution:
    def reverseBits(self, n: int) -> int:
        count = 0
        ans = 0
        while n > 0:
            ans = ans * 2 + (n % 2)
            n //= 2
            count += 1
        ans = ans << (32 - count)
        return ans
        