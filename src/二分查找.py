# -*-coding:utf-8 -*-
# Author     ：wangdahua
# Email      ：wangsh.a0bb@gmail.com
# Time       ：2022/11/26 22:12

from typing import List


# leetcode url: https://leetcode.cn/problems/binary-search/
# 标签：数组
class Solution:
    def binary_search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.binary_search([1, 2, 3, 4, 5], 4))
    print(s.binary_search([1, 2, 3, 4, 5], 6))
    print(s.binary_search([], 4))
