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
        n = len(intervals)
        intervals.sort(key = lambda x : x.start)
        prev_end = intervals[0].end
        for i in range(1, n):
            if intervals[i].start < prev_end:
                return False
            prev_end = intervals[i].end
        
        return True
