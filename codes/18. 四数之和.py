from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        if len(nums) < 4:
            return res

        for a in range(len(nums) - 3):
            # 优化
            if nums[a] + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:
                break
            if nums[a] + nums[len(nums) - 1] + nums[len(nums) - 2] + nums[len(nums) - 3] < target:
                continue
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, len(nums) - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                c, d = b + 1, len(nums) - 1
                while c < d:
                    sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if sum == target:
                        lst = [nums[a], nums[b], nums[c], nums[d]]
                        if not lst in res:  # 这里直接看数组是不是在res集里了
                            res.append(lst)
                        res.append(lst)
                        c += 1
                        # 当相等的时候，必须跳过重复数字
                        # while c < d and nums[c] == nums[c - 1]:  # 跳过重复数字
                        #     c += 1
                        d -= 1

                        # while d > c and nums[d] == nums[d + 1]:  # 跳过重复数字
                        #     d -= 1

                    # 不相等的时候，不可跳过重复数字，因为若nums[c]==nums[c+1],可能是d等于c+1的时候满足sum==target
                    elif sum < target:
                        c += 1
                    elif sum > target:
                        d -= 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.fourSum([0, 4, -5, 2, -2, 4, 2, -1, 4], 12))
    # 其实就相当于三数之和外面套了一层循环
