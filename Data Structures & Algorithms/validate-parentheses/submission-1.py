class Solution:
    def isValid(self, s: str) -> bool:
        opens = ["(", "{", "["]
        closed_to_open = {
            ")": "(",
            "}":"{",
            "]":"["
        }
        stack = []

        for i in range(len(s)):
            if not stack and s[i] not in opens:
                return False
            else: 
                if s[i] in opens:
                    stack.append(s[i])
                else:
                    open_bracket = stack.pop()
                    close_bracket = s[i]
                    if closed_to_open[close_bracket] == open_bracket:
                        continue
                    else:
                        return False
        
        if stack:
            return False
        return True
        