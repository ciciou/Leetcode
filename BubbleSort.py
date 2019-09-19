#-*-coding: utf-8 -*-
#author:cici
from typing import List
class Solution():
    #冒泡排序
    def BubbleSort(self,nums:List[int])->List[int]:
        num=len(nums)
        for i in range(num):
            for j in range(num-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums
    def BubbleSort_1(self,nums,start=0,end=None):
        if end is None:
            end=len(nums)-1
        if end<=start:
            return nums
        i,j=start,end
        num=nums[start] #作为参考点
        while j>i:
            if nums[j]>num:
                j=j-1
            else:
                nums[i],nums[j],nums[i+1]=nums[j],nums[i+1],nums[i]
                i=i+1
        Solution().BubbleSort_1(nums,start=start,end=i-1)
        Solution().BubbleSort_1(nums,start=i+1,end=end)
        return nums

if __name__=='__main__':
    nums=[10,9,2,-10,-18,7]
    print(Solution().BubbleSort_1(nums=nums))




