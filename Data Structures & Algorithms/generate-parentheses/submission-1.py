class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(open_brackets, closed_brackets):
            if open_brackets == closed_brackets == n:
                res.append("".join(stack))
                return
            if open_brackets < n:
                stack.append("(")
                backtrack(open_brackets + 1, closed_brackets)
                stack.pop()
            if closed_brackets < open_brackets:
                stack.append(")")
                backtrack(open_brackets, closed_brackets + 1)
                stack.pop()

        backtrack(0,0)
        return res