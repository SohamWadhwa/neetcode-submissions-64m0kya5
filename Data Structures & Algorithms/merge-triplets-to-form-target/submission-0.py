class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a_found, b_found, c_found = False, False, False
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            
            if a == target[0]:
                a_found = True
            if b == target[1]:
                b_found = True
            if c == target[2]:
                c_found = True
        return a_found and b_found and c_found
            