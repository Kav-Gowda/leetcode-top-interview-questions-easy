# LeetCode: Remove Duplicates from Sorted Array
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        write = 1

        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1

        return write

