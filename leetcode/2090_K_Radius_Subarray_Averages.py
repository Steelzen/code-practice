import math
# with prefix sum
def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1]) 
    
        ans = [0] * len(nums)
        for n in range(len(nums)):
            if n < k or n+k >= len(nums):
                ans[n] = -1
            elif n == k:
                ans[n] = math.trunc(prefix[n+k] / (2*k+1))
            else:
                ans[n] = math.trunc((prefix[n+k] - prefix[n-k-1]) / (2*k+1))
                #prefix index caution: n+k, n-k-1
        return ans

# with sliing wihdow
def getAverages2(self, nums: List[int], k: int) -> List[int]:
    averages = [-1] * len(nums)

    # When a single element is considered then its average will be itself
    if k == 0:
         return nums
     
    window_size = 2 * k + 1
    n = len(nums)

    # Any index will not have 'k' elements in it's left and right
    if window_size > n:
         return averages

    # First get the sum of first window of the 'nums' array
    window_sum = sum(nums[:window_size])
    averages[k] = window_sum // window_size

    # Iterate on rest indices which have at least 'k' elements on its left and right sides.
    for i in range(window_size, n):
         # 'i' is  the index of new inserted element, and 'i - window_size' is the index of the last removed element.
         window_sum = window_sum - nums[i - window_size] + nums[i]
         averages[i - k] = window_sum // window_size

    return averages     
    
