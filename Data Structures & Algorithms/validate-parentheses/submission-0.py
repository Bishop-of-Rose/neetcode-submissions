class Solution:
    def isValid(self, s: str) -> bool:
        stack = [None]
        mapping = {']': '[', '}': '{', ')': '('}
        for i in s:
            if i in '({[':
                stack.append(i)
                continue

            if stack[len(stack) - 1] == mapping[i]:
                stack.pop(len(stack) - 1)

            else:
                return False

        if stack != [None]:
            return False

        return True
                
                
        