class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and dic[s[i]] < dic[s[i + 1]]:
                res += dic[s[i + 1]] - dic[s[i]]
                i += 2
            else:
                res += dic[s[i]]
                i += 1

        return res


if __name__ == "__main__":
    s = Solution()
    mystring = str(input())

    # mystring = "MCMXCIV"
    result = s.romanToInt(mystring)
    print(result)
