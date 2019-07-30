#-*-coding: utf-8 -*-
#author:cici
class Solution():
    def romanToInt(self,s:str)->int:
        #思路：遍历每个字符，若是该字符对应的数字大于等于后一个对应的数字，则加，否则减
        #       末尾字符对应的数字直接加
        roman_dict={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        result=roman_dict[s[-1]]
        for index,char in enumerate(s[:-1]):
            if roman_dict[char]<roman_dict[s[index+1]]:
                result-=roman_dict[char]
            else:
                result+=roman_dict[char]
        return result

if __name__=='__main__':
    print(Solution().romanToInt("LVI"))