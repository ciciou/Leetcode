from typing import List
class Solution:
    def findRepeatNumber_1(self, nums: List[int]) -> int:
        #暴力解法双重for循环
        #dict1=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    #dict1.append(nums[i])
                    return nums[i]

    def findRepeatNumber_2(self, nums: List[int]) -> int:
        #先排序遇到相邻元素有相同的直接return
        nums.sort()
        num=nums[0]
        for n in range(1,len(nums)):
            if num==nums[n]:
                return num
            num=nums[n]

    def findRepeatNumber_3(self, nums: List[int]) -> int:
        dic={}
        for num in nums:
            if num not in dic:
                dic[num]=1
            else:
                return num


if __name__=='__main__':
    Solution().findRepeatNumber_3(nums=[2,1,3,2,5,3])