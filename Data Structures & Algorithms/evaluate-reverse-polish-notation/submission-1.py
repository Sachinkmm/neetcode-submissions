class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for op in tokens:
            if op in ["+", "-", "*", "/"]:
                if len(st) < 2:
                    continue
                v = int(st.pop())
                u = int(st.pop())
                if op == "+":
                    st.append(str(u+v))
                elif op == "-":
                    st.append(str(u-v))
                elif op == "*":
                    st.append(str(u*v))
                else:
                    st.append(str(int(u/v)))
            else:
                st.append(op)
        return int(st[-1])       