class Solution:
    def isPalindrome(self, x: int) -> bool:

        x_str = str(x)

        # 粗暴反转
        # if x_str == x_str[::-1]:
        #     return True
        # return False

        # 中心扩展
        # def expand(i, j):
        #     while i >= 0 and j < len(x_str) and x_str[i] == x_str[j]:  # 边界
        #         i -= 1
        #         j += 1
        #     return i + 1, j - 1
        #
        # i = len(x_str) // 2
        # left = right = 0
        # if not len(x_str) % 2:
        #     left, right = expand(i - 1, i)
        # else:
        #     left, right = expand(i, i)
        # if left == 0 and right == len(x_str) - 1:
        #     return True
        # return False

        # 数学反转 循环次数为x的位数向下取整，时间复杂度为O(lg n）
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10
        return x == reverted or x == reverted // 10


if __name__ == '__main__':
    s = Solution()
    x = int(input())

    # x = 121
    res = s.isPalindrome(x)
    print(res)
