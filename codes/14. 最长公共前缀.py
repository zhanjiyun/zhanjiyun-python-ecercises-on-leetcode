from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if not strs:
            return res
        isBreak = False
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(len(strs)):
                if i > len(strs[j]) - 1:
                    isBreak = True
                    break
                if strs[j][i] != c:
                    isBreak = True
                    break

            if isBreak:
                break
            res += c
        return res


if __name__ == "__main__":
    s = Solution()
    mystrings = str(input())
    strs = eval(mystrings)
    result = s.longestCommonPrefix(strs)
    print(result)
