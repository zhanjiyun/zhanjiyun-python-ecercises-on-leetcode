class Solution:
    def longestPalindrome(self, s: str) -> str:

        # 暴力循环
        # current_len = 0
        # max_len = 0
        # left = right = 0
        # for i in range(len(s)):
        #     for j in range(i + 1, len(s)):
        #         if i + max_len > len(s):
        #             break
        #         if s[i] == s[j]:
        #             s1 = s[i:j + 1]
        #             if s1[::-1] == s1:
        #                 current_len = j - i + 1
        #                 if current_len > max_len:
        #                     max_len = current_len
        #                     left = i
        #                     right = j
        #                 else:
        #                     pass
        # return s[left:right + 1]

        # 中心扩展法
        def expand(i: int, j: int):
            while i >= 0 and j < len(s) and s[i] == s[j]:  # 边界
                i -= 1
                j += 1
            return i + 1, j - 1

        left = right = 0

        for i in range(len(s)):
            l1, r1 = expand(i, i)  # 奇数扩展
            l2, r2 = expand(i, i + 1)  # 偶数扩展

            if r1 - l1 > right - left:
                left, right = l1, r1
            if r2 - l2 > right - left:
                left, right = l2, r2

        return s[left:right + 1]


if __name__ == '__main__':
    s = Solution()
    mystring = str(input())

    # mystring ="aaeee"
    result = s.longestPalindrome(mystring)
    print(result)
