# -*-coding:utf-8 -*-
# Author     ：wangdahua
# Email      ：wangsh.a0bb@gmail.com
# Time       ：2022/11/26 23:02
from typing import List


# leetcode url: https://leetcode.cn/problems/merge-sorted-array/
# 标签：数组
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        i = len(nums1) - 1
        m -= 1
        n -= 1
        while n >= 0:
            if m >= 0 and nums1[m] >= nums2[n]:
                nums1[m], nums1[i] = nums1[i], nums1[m]
                m -= 1
                i -= 1
            else:
                nums2[n], nums1[i] = nums1[i], nums2[n]
                n -= 1
                i -= 1
        # 这里是为了测试，return 一下
        return nums1


if __name__ == '__main__':
    # 这里特别要注意入参，注意题目中 nums1 的初始长度为 m + n
    s = Solution()
    print(s.merge([1, 2, 3, 0, 0], 3, [2, 5], 2))
    print(s.merge([5, 7, 9, 0], 3, [1], 1))
    print(s.merge([1, 2, 3], 3, [], 0))
