class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charmap = (
            set()
        )  # 定义charmap集合来保存子串，因为只需要判断字符是否重复，输出的是max_len，所以可以直接使用集合
        left = 0
        max_len = 0
        current_len = 0  # 当前子串长度
        for i in range(len(s)):
            current_len += 1
            while (
                s[i] in charmap
            ):  # while循环，删除子串中 与s[i]相同的字符 之前的所有字符以及 自身（后面会.add s[i]）
                current_len -= 1
                charmap.remove(s[left])
                left += 1  # 窗口右移
            charmap.add(s[i])
            max_len = max(max_len, current_len)
        return max_len


if __name__ == "__main__":
    s = Solution()
    my_str = str(input())

    # 测试集
    # my_str = "abcdba"
    result = s.lengthOfLongestSubstring(my_str)
    print(result)

# 滑动窗口
