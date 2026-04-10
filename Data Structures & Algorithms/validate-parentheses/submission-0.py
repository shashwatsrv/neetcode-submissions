class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}  # closing → opening map

        for char in s:
            if char in mapping:  # it's a closing bracket
                top = stack.pop() if stack else '#'  # '#' means invalid
                if mapping[char] != top:
                    return False
            else:  # it's an opening bracket
                stack.append(char)

        return not stack  # must be empty if valid
