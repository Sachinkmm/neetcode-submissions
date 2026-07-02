class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        maxFreq = max(count)
        maxCount = 0
        for i in count:
            if i == maxFreq:
                maxCount += 1
        
        time = (maxFreq - 1) * (n + 1) + maxCount
        return max(time, len(tasks))
        