class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # Memoization dictionary for power values
        memo = {1: 0}

        # Helper function to compute power value using recursion
        def power(x):
            if x not in memo:
                if x % 2 == 0:
                    memo[x] = 1 + power(x // 2)
                else:
                    memo[x] = 1 + power(3 * x + 1)
            return memo[x]

        # Generate all numbers in range [lo, hi]
        arr = list(range(lo, hi + 1))

        # Sort numbers by (power value, then number itself)
        arr.sort(key=lambda num: (power(num), num))

        # Return the k-th element (1-indexed)
        return arr[k - 1]
