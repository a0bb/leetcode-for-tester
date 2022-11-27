# -*-coding:utf-8 -*-
# Author     ：wangdahua
# Email      ：wangsh.a0bb@gmail.com
# Time       ：2022/11/27 10:46

# leetcode url: https://leetcode.cn/problems/palindrome-number/
# 标签：字符串、双指针

class Solution:
    """
    回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
    1.使用双指针，首先转成字符串
    2.初始位置，两个指针分别指向字符串两侧 left，right
    3.如果 x[left] != x[right] 返回 False；如果 x[left] == x[right] 则 left + 1,right - 1 后继续循环
    """
    def is_palindrome(self, x: int) -> bool:
        if x < 0:  # 如果小于 0，则是以负号开头，则不可能是回文字符串
            return False
        x = str(x)
        left = 0
        right = len(x) - 1
        while left < right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.is_palindrome(121))
    print(s.is_palindrome(123))
    print(s.is_palindrome(0))
    print(s.is_palindrome(-14-1))
