class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        n = len(s)

        for ch in s:
            if not st:
                st.append(ch)
                continue
            if (st[-1] == '(' and ch == ')') or (st[-1] == '[' and ch ==']') or (st[-1] == '{' and ch == '}'):
                st.pop()
            else:
                st.append(ch)
        
        if len(st) == 0:
            return True
        
        return False