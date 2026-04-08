class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t not in "+-*/":
                st.append(int(t))
            else:
                op1, op2 = int(st.pop()), int(st.pop())

                if t == '+':
                    st.append(op2 + op1)
                elif t == '-':
                    st.append(op2 - op1)
                elif t == '*':
                    st.append(op2 * op1)
                else:
                    st.append(int(op2 / op1))
        
        return st[-1]