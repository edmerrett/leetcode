'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:
- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
- arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
- arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true
'''
from typing import  List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        # Check if len of arr is less than 3 - not valid mountain array
        if len(arr) < 3:
            return False

        # set starting point as 2 element in the array
        i = 1

        # loop: if the element is smaller than the len of the array and 
        # the element is greater than the previous number -> upward slope
        while i < len(arr) and arr[i] > arr[i - 1]:
            i += 1

        # if i is 1 you have not moved or if i is the len of array you have moved too far
        if i == 1 or i == len(arr):
            return False

        # loop: if the element is smaller than the len of the array and
        # the element is smaller than the previous number -> downward slope
        while i < len(arr) and arr[i] < arr[i - 1]:
            i += 1

        # if you hve reached the end of the array successfully return True
        return i == len(arr)


s = Solution()
print(s.validMountainArray([0,3,4,5,3,2,1]))
