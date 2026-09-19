class Solution:

    def minLengthAfterRemovals(self, s: str) -> int:

        stack = []

        for ch in s:

            if stack and (
                (ch == 'a' and stack[-1] == 'b') or
                (ch == 'b' and stack[-1] == 'a')
            ):
                stack.pop()
            else:
                stack.append(ch)

        return len(stack)