import math

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        ans = left = 0
        curr = 1

        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1 # A

            ans += right - left + 1

        return ans
    
    def numSubarrayProductLessThanK2(self, nums: List[int], k: int) -> int:
        # using logharithm
        if k == 0:
            return 0
        k = math.log(k)
        
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + math.log(x))

        ans = 0
        for i, x in enumerate(prefix):
            j = bisect.bisect(prefix, x + k - 1e-9, i+1)
            ans += j - i - 1

        return ans        

