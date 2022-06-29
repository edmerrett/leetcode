'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

from typing import List

class MoveZeros:

    def MoveZerosBrute(self, arr: List[int]) -> List:
        '''
        Creates a new array, does not modify in-place
        '''
        sorted = []
        for i in arr:
            if i != 0:
                sorted.append(i)
        
        for r in range(len(sorted), len(arr)):
            sorted.append(0)
        
        return sorted
    
    def MoveZerosBetter(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0

        for int in arr:
            if int != 0:
                arr[j] = int
                j += 1
        
        for x in range(j, len(arr)):
            arr[x] = 0

m = MoveZeros()
print(m.MoveZerosBrute([0,1,0,3,12]))
print(m.MoveZerosBetter([0,1,0,3,12]))