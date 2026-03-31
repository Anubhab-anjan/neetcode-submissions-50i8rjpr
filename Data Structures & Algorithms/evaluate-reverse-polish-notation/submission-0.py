class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)  # Ensure integer division
        }
        for token in tokens:
            if token in operators:
                y=st.pop()
                x=st.pop()
                st.append(operators[token](x, y))
            else:
                st.append(int(token))
        return st[0]