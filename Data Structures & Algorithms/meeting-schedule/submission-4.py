"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda Interval:Interval.start)
        prevEnd = intervals[0].end
        for interval in intervals[1:]:
            if prevEnd > interval.start:
                return False
            else:
                prevEnd = interval.end
        return True
