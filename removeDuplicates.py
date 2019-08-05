#-*-coding: utf-8 -*-
#author:cici
from typing import List
class Solution():
    def removeDuplicates(self,nums:List[int])->int:
        #思路：list.remove(obj)移除指定项
        for num in nums:
            while nums.count(num)>1:
                nums.remove(num)
            else:
                pass
        return len(nums)

    def removeDuplicates_1(self,nums:List)->int:
        #思路：双指针（快慢指针）
        indexi=0
        indexj=1
        while indexj<len(nums):
            if nums[indexi]==nums[indexj]:
                nums.pop(indexj)
            else:
                indexi+=1
                indexj=indexi+1
        return len(nums)

    def removeDuplicates_2(self,nums:List[int])->int:
        #思路：list set sorted
        nums[:]=sorted(list(set(nums)))
        return len(nums)

if __name__=='__main__':
    print(Solution().removeDuplicates_2([0,0,1,1,1,2,4,5,5]))