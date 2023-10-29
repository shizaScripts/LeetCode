class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            elif s[i] == "[":
                stack.append(s[i])
            elif s[i] == "{":
                stack.append(s[i])

            elif s[i] == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(s[i])
            elif s[i] == "]":
                if stack and  stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(s[i])    
            elif s[i] == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(s[i])
        
        if not stack:
            return True
        else:

            return False
