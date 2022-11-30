# -*-coding:utf-8 -*-
# Author     ：wangdahua
# Email      ：wangsh.a0bb@gmail.com
# Time       ：2022/11/27 21:35
from typing import List


# leetcode url: https://leetcode.cn/problems/minimum-size-subarray-sum/
# 标签：数组、双指针、滑动窗口


class Solution:
    """
    滑动窗口题
    1.窗口内的数字总和 sum < target，窗口右边就一直向右滑动
    2.当 sum >= target 的时候，窗口左边开始往右滑动，同时 sum 需要减去滑动过的数字
    """
    def min_sub_array_len(self, nums: List[int], target: int) -> int:
        left = 0  # 窗口的左边
        result = float('inf')
        sum_ = 0
        for right in range(len(nums)):  # right 为窗口的右边
            sum_ += nums[right]
            while sum_ >= target:
                result = min(result, right - left + 1)
                sum_ -= nums[left]
                left += 1
        return 0 if result == float('inf') else result


if __name__ == '__main__':
    s = Solution()
    print(s.min_sub_array_len([1, 2, 3, 4, 5], 5))
