from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k

        # dp[r] = number of subarrays ending at the previous position
        # whose product % k == r
        dp = [0] * k

        for num in nums:
            num %= k

            new_dp = [0] * k

            # Start a new subarray: [num]
            new_dp[num] += 1

            # Extend previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * num) % k
                    new_dp[new_r] += dp[r]

            # Add all subarrays ending at this position
            for r in range(k):
                result[r] += new_dp[r]

            dp = new_dp

        return result