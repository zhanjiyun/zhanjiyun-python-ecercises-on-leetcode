from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not len(nums) >= 3:
            return []
        res = []

        # 依旧暴力，三层循环
        # i = j = k = 0
        # for a in range(len(nums) - 2):
        #     for b in range(a + 1, len(nums) - 1):
        #         for c in range(b + 1, len(nums)):
        #             if nums[a] + nums[b] + nums[c] == 0:
        #                 lst = [nums[a], nums[b], nums[c]]
        #                 lst = sorted(lst)
        #                 if not lst in res:
        #                     res.append(lst)

        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    while j < k and nums[j + 1] == nums[j]:
                        j += 1
                    while j < k and nums[k - 1] == nums[k]:
                        k -= 1
                    lst = [nums[i], nums[j], nums[k]]
                    # 这里最初这种判断时间复杂度较高
                    # if not lst in res:
                    res.append(lst)
                    k -= 1
                    j += 1
                elif sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
        return res


if __name__ == "__main__":
    s = Solution()
    nums = eval(input())

    # 测试
    # nums = [-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0]
    result = s.threeSum(nums)
    print(result)
