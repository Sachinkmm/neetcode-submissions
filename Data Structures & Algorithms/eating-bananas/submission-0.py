class Solution:
    def isPossible(self, k, piles, h):
        time_to_eat = 0
        for val in piles:
            time_to_eat += math.ceil(val / k)
            if time_to_eat > h:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = 1e10
        while l <= r:
            mid = (l + r) // 2
            if self.isPossible(mid, piles, h):
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans
        