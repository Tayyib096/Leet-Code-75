class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for e in s:
            if(e != ']'):
                stack.append(e)
            else:
                curr = ''
                while stack and stack[-1] != '[':
                    curr = stack.pop()+curr
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(curr * int(num))

        return (''.join(stack))