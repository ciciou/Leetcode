from typing import List
class Solution():
    def longestCommonPrefix(self,strs:List[str])->str:
        #思路：利用zip,zip函数:将对象中对应的元素打包成一个个元组
        result=''
        for tup in zip(*strs):
            count=0
            for t in tup:
                if tup[0]!=t:
                    break
                count+=1
            if count!=len(tup):
                break
            result=f"{result}{tup[0]}"
        return result

    def longestCommonPrefix_1(self,strs:List[str])->str:
        #set函数：返回一个无无序不重复元素集
        result=''
        for tup in zip(*strs):
            if len(set(tup))!=1:
                break
            result=f"{result}{tup[0]}"
        return result

    def longestCommonPrefix_2(self,strs:List[str])->str:
        if not strs:
            return ""
        max_str=max(strs)
        min_str=min(strs)
        print(max_str)
        print(min_str)
        for index,char in enumerate(min_str):
            if char!=max_str[index]:
                return min_str[:index]
        return min_str

if __name__=='__main__':
    str1=['cici','ciabby','cigray']
    print(Solution().longestCommonPrefix_2(strs=str1))
