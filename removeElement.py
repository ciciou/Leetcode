#-*-coding: utf-8 -*-
#author:cici
from typing import List
class Solution():
    def removeElement(self,nums:List[int],val:int)->int:
        for num in nums:
            if num==val:
                nums.remove(2)
            else:
                pass
        return len(nums)
    def removeElement_1(self,nums:List[int],val:int)->int:
        while val in nums:
            nums.remove(val)
        return len(nums)


if __name__=='__main__':
    print(Solution().removeElement_1([2,3,2,3],2))