class Solution:
        def fib(self, n: int) -> int:
            def feb(n):
                if n==0:
                    return 0
                if n==1:
                    return 1
                return feb(n-1)+feb(n-2)
            return feb(n)