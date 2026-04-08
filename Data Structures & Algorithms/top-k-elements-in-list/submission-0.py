class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        count = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freq[num] += 1
        for num, cnt in freq.items():
            count[cnt].append(num)
        
        res = []
        for i in range(len(count) - 1, -1, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return []