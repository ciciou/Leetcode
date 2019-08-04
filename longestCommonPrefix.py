from typing import List
class Solution():
    def longestCommonPrefix(self,strs:List[str])->str:
        #思路：利用zip
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
        result=''
        for tup in zip(*strs):
            if len(set(tup))!=1:
                break
            result=f"{result}{tup[0]}"
        return result

if __name__=='__main__':
    str1=['cici','ciabby','cigray']
    print(Solution().longestCommonPrefix_1(strs=str1))
