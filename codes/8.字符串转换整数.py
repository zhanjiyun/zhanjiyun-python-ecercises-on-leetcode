class solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        s = s.strip()
        flag = 1
        result = ''

        if not s:
            return 0

        # if s[0] == '-':
        #     flag = -1
        #     s = s[1:]
        # elif s[0] == '+':
        #     flag = 1
        #     s = s[1:]
        # elif not s[0].isdigit():
        #     return 0
        # for char in s:
        #     if not char.isdigit():
        #         break
        #     else:
        #         result += char
        #
        # result = int(result) * flag
        # result = max(min(result, INT_MAX), INT_MIN)
        # return result

        i = 0

        if s[0] == '-':
            flag = -1
            i += 1
        if s[0] == '+':
            flag = 1
            i += 1
        while i < len(s) and s[i].isdigit():
            dight = int(s[i])
            result = result * 10 + dight
            i += 1
        result *= flag
        result = max(min(result, INT_MAX), INT_MIN)
        return result


if __name__ == '__main__':
    s = solution()
    mystring = str(input())

    # mystring = "   -042"
    result = s.myAtoi(mystring)
    print(result)
