'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

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
'''
from typing import List

class Solution:
    def twoSumLoop(self, nums: List[int], target: int) -> List[int]:
        ''' O(n^2) '''
        for i in range(len(num_arr) - 1):
            for j in range(i + 1, len(num_arr)):
                if num_arr[i] + num_arr[j] == pair_sum:
                    print("Loop:", [i, j])
                    return([i, j])


    def twoSumHash(self, nums: List[int], target: int) -> List[int]:
        ''' O(n) '''
        seen = {}
        for i, element in enumerate(num_arr):
            comp = pair_sum - element
            if comp in seen:
                print("Hash:", [seen[comp], i])
                return([seen[comp], i])
            elif element not in seen:
                seen[element] = i

num_arr = [3, 5, 2, 8, 11]
pair_sum = 7

two_sum = Solution()
two_sum.twoSumLoop(num_arr, pair_sum)
two_sum.twoSumHash(num_arr, pair_sum)
