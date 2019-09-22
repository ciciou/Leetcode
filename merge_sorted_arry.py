from typing import List
class Solution():
    def merge_sorted_arry(self,arry1:List[int],arry2:List[int])->List[int]:
        #思路：有序列表，exten()扩展新列表
        arry=[]
        i,j=0,0
        while True:
            if i==len(arry1):
                arry.extend(arry2[j:])
                return arry
            elif j==len(arry2):
                arry.exten(arry1[i:])
                return arry
            else:
                if arry1[i]<arry2[j]:
                    arry.append(arry1[i])
                    i=i+1
                else:
                    arry.append(arry2[j])
                    j=j+1
    def merge_sorted_arry_1(self,arry1:List[int],arry2:List[int])->List[int]:
        #思路：扩张列表后使用冒泡排序
        arry1.extend(arry2)
        a=len(arry1)
        for i in range(a):
            for j in range(a-i-1):
                if arry1[j]>arry1[j+1]:
                    arry1[j],arry1[j+1]=arry1[j+1],arry1[j]
        return arry1
if __name__=='__main__':
    print(Solution().merge_sorted_arry_1(arry1=[-1,2,3,5,6],arry2=[-2,2,5,7,8]))