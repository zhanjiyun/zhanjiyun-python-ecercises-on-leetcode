from typing import List


# 引入∞防止数组越界
def get_val(arr, idx):
    if idx < 0:
        return float('-inf')
    if idx >= len(arr):
        return float('inf')
    return arr[idx]


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_total = len(nums1) + len(nums2)

        # 暴力求解
        # left = (len_total+ 1) // 2
        # right = (len_total + 2) // 2
        # s = sorted(nums1 + nums2)
        # mid = (s[left - 1] + s[right - 1]) / 2
        # return mid

        if len(nums1) > len(nums2):  # 根据长度调整先后
            nums1, nums2 = nums2, nums1

        # 一开始想 讨论空数组的情况，后来引入数组越界发现用∞覆盖了这个讨论
        # if len(nums1) == 0:
        #     if len(nums2) % 2:
        #         result = nums2[len(nums2) // 2]
        #     else:
        #         result = (nums2[len(nums2) // 2] + nums2[len(nums2) // 2 - 1]) / 2
        #     return result

        i = len(nums1)
        j = len_total // 2 - i  # 这里划分左右时，偷个懒直接把短数组全部放在左边

        left = [get_val(nums1, i - 1), get_val(nums2, j - 1)]
        right = [get_val(nums1, i), get_val(nums2, j)]

        while max(left) > min(right):
            if get_val(nums1, i - 1) <= get_val(nums2, j - 1):
                i += 1
                j -= 1
            else:
                i -= 1
                j += 1
            left = [get_val(nums1, i - 1), get_val(nums2, j - 1)]
            right = [get_val(nums1, i), get_val(nums2, j)]
        num_mid = (max(left) + min(right)) / 2 if not len_total % 2 else min(right)
        return num_mid


if __name__ == '__main__':
    s = Solution()
    nums1 = eval(str(input()))
    nums2 = eval(str(input()))

    # 测试集
    # nums1 = []
    # nums2 = [2, 3, 4, 5, 5]

    print(s.findMedianSortedArrays(nums1, nums2))
