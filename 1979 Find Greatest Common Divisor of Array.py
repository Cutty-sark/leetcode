import math

class Solution:
    def findGCD(self, nums: List[int]) -> int:

        small = min(nums)
        big = max(nums)

        return math.gcd(small, big)