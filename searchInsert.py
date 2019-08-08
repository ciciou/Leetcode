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

if __name__=='__main__':
    print(Solution().searchInsert([1,3,6,7],5))

