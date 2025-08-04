import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return bool(re.fullmatch(p, s))  # 这里直接偷懒用了re库


if __name__ == "__main__":
    solution = Solution()
    s = str(input())
    p = str(input())

    # 测试集
    # s = "aab"
    # p = "c*a*b"
    result = solution.isMatch(s, p)
    print(result)
