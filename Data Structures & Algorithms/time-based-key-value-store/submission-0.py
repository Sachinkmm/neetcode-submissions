class TimeMap:

    def __init__(self):
        self.time_map = {} # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        l = 0
        r = len(self.time_map[key]) - 1
        ans = ""
        while l <= r:
            m = (l + r) // 2
            if self.time_map[key][m][1] == timestamp:
                return self.time_map[key][m][0]
            elif self.time_map[key][m][1] < timestamp:
                ans = self.time_map[key][m][0]
                l = m + 1
            else:
                r = m - 1
        return ans
        
