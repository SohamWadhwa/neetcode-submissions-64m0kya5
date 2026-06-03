"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        timeline = []
        for i in intervals:
            timeline.append((i.start, 1))
            timeline.append((i.end, -1))
        
        timeline.sort(key=lambda x: (x[0], x[1]))

        res = curr = 0
        for t in timeline:
            curr += t[1]
            res = max(res, curr)
        return res