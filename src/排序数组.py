# -*-coding:utf-8 -*-
# Author     ：wangdahua
# Email      ：wangsh.a0bb@gmail.com
# Time       ：2022/11/26 23:47
import random
from typing import List


# leetcode url: https://leetcode.cn/problems/sort-an-array/
# 标签：数组、排序
class Solution:
    # 快排
    def quick_sort(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        self.recursion(nums, left, right)
        return nums

    def recursion(self, nums, left, right):
        if left >= right:
            return
        pivot_index = self.partition(nums, left, right)
        self.recursion(nums, left, pivot_index - 1)
        self.recursion(nums, pivot_index + 1, right)

    def partition(self, nums, left, right):
        pivot_index = random.randint(left, right)
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        pivot = nums[right]
        slow = left
        for fast in range(left, right):
            if nums[fast] < pivot:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        nums[right], nums[slow] = nums[slow], nums[right]
        return slow


if __name__ == '__main__':
    s = Solution()
    print(s.quick_sort([]))
    print(s.quick_sort([1, 2, 3, 6, 4, 3]))
    print(s.quick_sort([1, 2, 3, 6, 4, -1]))

