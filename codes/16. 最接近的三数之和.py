from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        diff = float('inf')  # 差值提前无穷大
        res = 0

        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                current_diff = abs(target - sum)
                if current_diff < diff:
                    diff = current_diff
                    res = sum
                if sum - target > 0:
                    k -= 1
                else:
                    j += 1
        return res


# 跟上一题一样，还是循环i，jk双指针移动

if __name__ == '__main__':
    s = Solution()
    nums = [4, 0, 5, -5, 3, 3, 0, -4, -5]
    target = -2
    result = s.threeSumClosest(nums, target)
    print(result)
