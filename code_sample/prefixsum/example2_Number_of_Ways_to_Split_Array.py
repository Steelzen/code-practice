class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        # prefix sum
        n = len(nums)
        prefix = [nums[0]]

        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])

        ans = 0
        for i in range(n - 1):
            left_section = prefix[i]
            right_section = prefix[-1] - prefix[i]
            if left_section >= right_section:
                ans += 1

        return ans
    
    def waysToSplitArray2(self, nums: list[int]) -> int:
        ans = left_section = 0
        total = sum(nums)

        for i in range(len(nums) - 1):
            left_section += nums[i]
            right_section = total - left_section
            if left_section >= right_section:
                ans += 1

        return ans        


if __name__ == "__main__":
    my_list = [10, 4, -8, 7]
    ans = Solution().waysToSplitArray(my_list)
    ans2 = Solution().waysToSplitArray2(my_list)

    print(ans)
    print(ans2)
    