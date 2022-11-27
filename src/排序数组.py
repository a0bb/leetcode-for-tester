# -*-coding:utf-8 -*-
# Author     ：wangdahua
# Email      ：wangsh.a0bb@gmail.com
# Time       ：2022/11/26 23:47
import random


# leetcode url: https://leetcode.cn/problems/sort-an-array/
# 标签：数组、排序

class Solution:
    """ 快排
    1.确定排序的区间 [left, right]
    2.找到分区点，把比分区点的值小的数放在分区点左边，把比分区点的值大的数放在分区点的右边
    3.分别按照 2 的逻辑去递归分区点的左边区域和右边区域
    4.当 left >= right 的时候，结束递归
    """

    def quick_sort(self, nums):
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
            # 这里的右边界为什么不用 right + 1，因为 nums[right] 被抓去做分区点 pivot 了
            if nums[fast] < pivot:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        nums[slow], nums[right] = nums[right], nums[slow]
        return slow


if __name__ == '__main__':
    s = Solution()
    print(s.quick_sort([]))
    print(s.quick_sort([1, 2, 3, 6, 4, 3]))
    print(s.quick_sort([1, 2, 3, 6, 4, -1]))

