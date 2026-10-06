class Solution:
    def kthCharacter(self, k: int) -> str:

        def rec(ch):

            if len(ch) >= k:
                return ch

            val = ""

            for char in ch:
                val += chr(ord(char) + 1)

            ch = ch + val

            return rec(ch)

        ch = "a"

        result = rec(ch)

        return result[k - 1]