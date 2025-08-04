class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        # # 依旧暴力
        # rows = numRows
        # l = len(s)
        # cols = (len(s) // (numRows * 2 - 2) + 1) * (numRows - 1)
        # lst = [['0' for _ in range(cols)] for _ in range(rows)]
        # result = ''
        #
        # current_col = i = 0
        # while i < len(s):
        #     for j in range(numRows): # 整列向下
        #         if not i < len(s):
        #             break
        #         lst[j][current_col] = s[i]
        #         i += 1
        #     current_col += 1
        #
        #     for k in range(numRows - 2, 0, -1): # 斜向右上
        #         if not i < len(s):
        #             break
        #         lst[k][current_col] = s[i]
        #         i += 1
        #         current_col += 1
        #
        # for i in range(rows):
        #     for j in range(cols):
        #         if lst[i][j] != '0':
        #             result += lst[i][j]

        i = 0
        direction = -1  # 控制方向
        rows = ["" for i in range(numRows)]
        for char in s:
            rows[i] += char
            if i == numRows - 1 or i == 0:
                direction *= -1
            i += direction

        result = "".join(rows)
        return result


if __name__ == "__main__":
    s = Solution()
    mystring = str(input())
    n = int(input())
    result = s.convert(mystring, n)

    # 测试机
    # result = s.convert("AB", 1)
    print(result)
