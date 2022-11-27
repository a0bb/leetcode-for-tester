# -*-coding:utf-8 -*-
# Author     ：wangdahua
# Email      ：wangsh.a0bb@gmail.com
# Time       ：2022/11/27 11:33

# leetcode url: https://leetcode.cn/problems/valid-palindrome/
# 标签：字符串、双指针

class Solution:
    """
    验证回文串
    1.先把 s 移除所有的非字母数字字符，然后转为小写
    2.后面逻辑与题目“回文数”一样
    """
    def is_palindrome(self, s: str):
        s = [c.lower() for c in s if c.isalnum()]
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.is_palindrome('A man, a plan, a canal: Panama'))
    print(s.is_palindrome('1 1'))
    print(s.is_palindrome('race a car'))
