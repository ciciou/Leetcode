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

    def twoSum_3(self,nums:List[int],target:int)->List[int]:
        #最优解
        d1={}
        for i in range(len(nums)):
            a=target-nums[i]
            if a in d1:
                return [d1[a],i]
            d1[nums[i]]=i

    def twoSum_4(self,nums:List[int],target:[int])->List[int]:
        d2={}
        a=0
        while nums[a] not in d2:
            d2[target-nums[a]]=a
            a=a+1
        return [d2[nums[a]],a]

    def twoSum_5(self, nums: List[int], target: [int]) -> List[int]:
        d3={}
        for b in range(len(nums)):
            c=target-nums[b]
            if c in d3:
                return [d3[c],b+1]
            d3[nums[b]]=b+1
if __name__=='__main__':
    nums=[2,10,12,16,17]
    target=28
    print(Solution().twoSum_5(nums=nums, target=target))






