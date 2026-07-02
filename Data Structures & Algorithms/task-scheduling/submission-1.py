class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count = [0] * 26
        # for task in tasks:
        #     count[ord(task) - ord('A')] += 1
        
        # maxFreq = max(count)
        # maxCount = 0
        # for i in count:
        #     if i == maxFreq:
        #         maxCount += 1
        
        # time = (maxFreq - 1) * (n + 1) + maxCount
        # return max(time, len(tasks))
        count = Counter(tasks)
        pq = []
        for cnt in count.values():
            heapq.heappush(pq, -1 * cnt)
        
        time = 0
        q = deque() # pair of [-cnt, idleTime]
        while pq or q:
            time += 1

            if not pq:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(pq)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(pq, q.popleft()[0])

        return time
        