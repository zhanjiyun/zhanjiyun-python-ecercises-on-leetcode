from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 暴力解法，两次循环
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]

        # 哈希表
        hashmap = {}
        for i in range(len(nums)):
            nums_needed = target - nums[i]
            if nums_needed in hashmap:
                return [hashmap[nums_needed], i]
            hashmap[nums[i]] = i
        return [] #找不到两数之和为target

if __name__ == '__main__':
    s = Solution()
    nums_str = input()
    target = int(input())
    nums = eval(nums_str)

    # 测试
    # nums = [2, 7, 11, 15]
    # target = 9

    print(s.twoSum(nums, target))