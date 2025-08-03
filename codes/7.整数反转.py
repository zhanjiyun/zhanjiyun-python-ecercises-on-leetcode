class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        flag = 1 if x >= 0 else -1  # 符号标志
        x = abs(x)  # 直接取正数
        x_str = str(x)
        reversedx_str = x_str[::-1]
        reversedx = int(reversedx_str) * flag

        if reversedx > INT_MAX or reversedx < INT_MIN:  # 溢出判断
            return 0

        return reversedx


if __name__ == '__main__':
    s = Solution()
    num = int(input())
    result = s.reverse(num)
    print(result)
