from typing import List
class Solution:
    def twoSum(self, nums : List[int], target:int)-> List[int]:
        num = []
        l = len(nums)
        for i in range(l):
            for j in range(i+1,l):
                if nums[i] + nums[j] == target:
                    num.append(i)
                    num.append(j)
                    return num
    def twoSum_1(self, nums : List[int], target:int) -> List[int]:
        for num in nums:
            try:
                a = nums.index(num)
                b = nums.index(target - num, a + 1)
                return [a, b]
            except Exception as e:
                print('twoSum is fail',format(e))
    def twoSum_2(self,nums:List[int],target:int)->List[int]:
        for i in range(len(nums)):
            if (target-nums[i]) in nums[i+1:]:
                return [i,nums.index(target-nums[i],i+1)]
if __name__=='__main__':
    nums=[2,10,12,16,17]
    target=28
    print(Solution().twoSum_1(nums=nums, target=target))






