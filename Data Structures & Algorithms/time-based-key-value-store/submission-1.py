from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        n = len(self.timeMap[key])
        arr = self.timeMap[key]

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][1] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        
        if r < 0:
            return ""
        return arr[r][0]

