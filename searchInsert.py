#-*-coding: utf-8 -*-
#author:cici
from typing import List
class Solution():
    def searchInsert(self,nums:List[int],target:int)->int:
        for index,num in enumerate(nums):
            if target<=num:
                return index
            else:
                pass
    def searchInsert_1(self,nums:List[int],target:int)->int:
        #思路：二分查找
        left=0
        right=len(nums)
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid
        return left
if __name__=='__main__':
    print(Solution().searchInsert_1([1,3,6,7],5))

