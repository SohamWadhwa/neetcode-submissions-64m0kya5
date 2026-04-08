class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []

        res = [0] * n

        for i in range(n - 1, -1, -1):
            while st and st[-1][0] <= temperatures[i]:
                st.pop()
            
            if st and temperatures[i] < st[-1][0]:
                res[i] = st[-1][1] - i
            
            st.append([temperatures[i], i])
        
        return res
