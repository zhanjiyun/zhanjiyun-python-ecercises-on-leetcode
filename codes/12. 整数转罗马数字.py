class Solution:
    def intToRoman(self, num: int) -> str:
        # 暴力解法 直接递归
        # if num >= 1000:
        #     return "M" * (num // 1000) + self.intToRoman(num % 1000)
        # elif num >= 900:
        #     return "CM" + self.intToRoman(num % 900)
        # elif num >= 500:
        #     return "D" * (num // 500) + self.intToRoman(num % 500)
        # elif num >= 400:
        #     return "CD" + self.intToRoman(num % 400)
        # elif num >= 100:
        #     return "C" * (num // 100) + self.intToRoman(num % 100)
        # elif num >= 90:
        #     return "XC" + self.intToRoman(num % 90)
        # elif num >= 50:
        #     return "L" * (num // 50) + self.intToRoman(num % 50)
        # elif num >= 40:
        #     return "XL" + self.intToRoman(num % 40)
        # elif num >= 10:
        #     return "X" * (num // 10) + self.intToRoman(num % 10)
        # elif num >= 9:
        #     return "IX"
        # elif num >= 5:
        #     return "V" + "I" * (num - 5)
        # elif num >= 4:
        #     return "IV"
        # elif num >= 1:
        #     return "I" * num
        # else:
        #     return ""

        # 贪心算法
        lst = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        out = ""
        for number, rom in lst:
            while number <= num:
                num -= number
                out += rom
                if num == 0:
                    break
        return out


if __name__ == "__main__":
    s = Solution()
    num = int(input())

    # num = 3749
    result = s.intToRoman(num)
    print(result)
