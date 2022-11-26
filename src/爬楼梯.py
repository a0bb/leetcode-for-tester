# -*-coding:utf-8 -*-
# Author     ：wangdahua
# Email      ：wangsh.a0bb@gmail.com
# Time       ：2022/11/26 23:27

# leetcode url: https://leetcode.cn/problems/climbing-stairs/
# 标签：递归、动态规划

class Solution:
    def climb_stairs(self, n: int):
        # 递归公式：dp[i] = dp[i - 1] + dp[i - 2]
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.climb_stairs(1))
    print(s.climb_stairs(2))
    print(s.climb_stairs(3))
    print(s.climb_stairs(10))
