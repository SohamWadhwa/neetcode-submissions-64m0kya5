class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        my_set = set()
        max_cnt = 1

        for num in nums:
            my_set.add(num)
        
        for num in nums:
            if num - 1 not in my_set:
                el = num
                cnt = 1
                while el + 1 in my_set:
                    el = el + 1
                    cnt += 1
                max_cnt = max(max_cnt, cnt)
        
        return max_cnt