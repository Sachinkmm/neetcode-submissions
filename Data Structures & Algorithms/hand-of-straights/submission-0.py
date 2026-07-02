class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        mp = defaultdict(int)
        hand.sort()
        for num in hand:
            mp[num] += 1
        
        for num in hand:
            if mp[num] > 0:
                for i in range(num, num + groupSize):
                    if mp[i] == 0:
                        return False
                    mp[i] -= 1
        return True