from typing import List
class Solution():
    def Look(self,nums:List[int],target:int)->int:
        if target in nums:
            return nums.index(target)
        else:
            pass

    def Look_1(self, nums: List[int], target: int) -> int:
        for i in nums:
            if i==target:
                return nums.index(target)
            else:
                pass

    def Look_2(self, nums: List[int], target: int)->int:
        start,end=0,len(nums)-1
        while True:
            if end-start <=1:
                if target==nums[start]:
                    return start
                if target==nums[end]:
                    return end
            mid=(end+start)//2
            if nums[mid]>=target:
                end=mid
            else:
                start=mid

if __name__=='__main__':
    print(Solution().Look_2(nums=[1,3,5,8,10,15],target=10))