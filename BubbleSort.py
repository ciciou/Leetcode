#-*-coding: utf-8 -*-
#author:cici
from typing import List
class Solution():
    def BubbleSort(self,nums:List[int])->List[int]:
        num=len(nums)
        for i in range(num):
            for j in range(num-1-i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums
if __name__=='__main__':
    nums=[10,9,-10,6,19,2,-18]
    print(Solution().BubbleSort(nums=nums))




