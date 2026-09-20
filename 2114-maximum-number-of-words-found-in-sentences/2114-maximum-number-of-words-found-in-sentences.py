class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        m=0
        for ch in sentences:
            ch=ch.split(" ")
            m=max(m,len(ch))
        return m