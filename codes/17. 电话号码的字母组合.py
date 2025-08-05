from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        lst = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        # 直接循环 从外往内找
        # res = [""]  # 初始结果是空字符串 否则无法循环
        # for char in digits:
        #     num = int(char)
        #     temp = []
        #     for i in res:
        #         for l in lst[num]:
        #             temp.append(i + l)
        #     res = temp
        # return res

        # 回溯 从内往外找
        res = []

        def backtrack(index: int, path: str):
            if index == len(digits):
                res.append(path)
                return
            for letter in lst[int(digits[index])]:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return res


if __name__ == '__main__':
    s = Solution()
    digits = "23"
    result = s.letterCombinations(digits)
    print(result)
