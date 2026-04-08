class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        pse, nse = [-1] * n, [n] * n

        st = []
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                pse[i] = st[-1]
            st.append(i)
        st = []
        for i in range(n - 1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                nse[i] = st[-1]
            st.append(i)
        
        maxAr = 0
        for i in range(n):
            width = nse[i] - pse[i] - 1
            maxAr = max(maxAr, heights[i] * width)
        return maxAr