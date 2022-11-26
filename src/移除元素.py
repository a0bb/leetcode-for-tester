# -*-coding:utf-8 -*-
# Author     ：wangdahua
# Email      ：wangsh.a0bb@gmail.com
# Time       ：2022/11/26 22:19
from typing import List


# leetcode url: https://leetcode.cn/problems/remove-element/
# 标签：数组

# 使用快慢指针解决此问题，快指针来遍历数组，慢指针用来收集不等于 val 的元素
class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        """
        移除目标元素
        :param nums:
        :param val:
        :return: 移除后数组的新长度
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow


if __name__ == '__main__':
    s = Solution()
    print(s.remove_element([1, 2, 3, 4, 5, 2], 2))
    print(s.remove_element([1, 2, 3, 4, 5, 2], -1))
    print(s.remove_element([], -1))
