# -*-coding:utf-8 -*-
# Author     ：wangdahua
# Email      ：wangsh.a0bb@gmail.com
# Time       ：2022/11/27 20:53
from typing import List


# leetcode url: https://leetcode.cn/problems/squares-of-a-sorted-array/
# 标签：数组、双指针

class Solution:
    """
    有序数组的平方
    题目关键词：非递减顺序
    1.注意：整数数组内，可能包含负数
    2.平方之后最大值一定产生在数组的左侧或者右侧
    3.左侧平方 lm，右侧平方 rm，如果 lm > rm，则把 lm 放到新数组，反之，则把 rm 放到新数组
    """

    def sorted_squares(self, nums: List[int]):
        n = len(nums)
        left = 0
        right = n - 1
        ans = [0] * n
        i = n - 1
        while left <= right:
            lm = nums[left] ** 2
            rm = nums[right] ** 2
            if lm > rm:
                ans[i] = lm
                left += 1
            else:
                ans[i] = rm
                right -= 1
            i -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.sorted_squares([-4, -3, 0, 3, 5]))
    print(s.sorted_squares([]))
    print(s.sorted_squares([1, 2, 3, 4, 5]))
