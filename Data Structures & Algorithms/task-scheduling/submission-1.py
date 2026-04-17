class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for t in tasks:
            count[ord(t) - ord('A')] += 1
        
        maxFreq = max(count)
        maxCount = 0
        for cnt in count:
            maxCount += 1 if cnt == maxFreq else 0

        time = (maxFreq - 1) * (n + 1) + maxCount
        return max(len(tasks), time)