class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if stack:
                # if last item is equal to an uppercase or lowercase version of char
                # pop the character
                if stack[-1] != char and (stack[-1] == str.lower(char) or stack[-1] == str.upper(char)):
                    stack.pop()
                else:
                    stack.append(char)
            # otherwise add the normal character
            else:
                stack.append(char)
        return ''.join(stack)

                    
            
        