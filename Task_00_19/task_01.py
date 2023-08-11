# -*- coding: utf-8 -*-
"""
1. Two Sum


Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""
import time


def main(nums: list[int], target: int) -> list[int]:
    """
    O(n^2 / 2)
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    length = len(nums)
    for num1 in range(length):
        for num2 in range(num1+1, length):
            if nums[num1] + nums[num2] == target:
                return [num1, num2]


def faster_main(nums: list[int], target: int) -> list[int]:
    """
    O(n^2 / 2)
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for idx in range(len(nums)):
        if (num := (target - nums[idx])) in nums[idx+1:]:
            return [idx, nums.index(num, idx+1)]


def fastest_main(nums: list[int], target: int) -> list[int]:
    """
    O(n)
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        seen[nums[i]] = i


if __name__ == '__main__':
    start_time = time.time()
    print(f'Final Number: {fastest_main([-1,-2,-3,-4,-5], -8)}')
    print(f'--- {(time.time() - start_time)} seconds ---')
