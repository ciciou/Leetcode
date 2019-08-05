class Solution():
    def isValid(self,s:str)->bool:
        # 思路：数组模拟栈，遍历字符串与栈顶元素对比，配对上进行出栈操作，否则入栈操作
        if not s:
            return True
        map = {'(': ')', '{': '}', '[': ']'}
        result = []
        for index in range(len(s)):
            if len(result)==0 or s[index]!=map.get(result[len(result)-1],""):
                result.append(s[index])
            else:
                result.pop()
        return not bool(result)
    def isValid_1(self,s:str)->bool:
        stack=[]
        dict={'()', '{}', '[]'}
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if stack[-1]+i in dict:
                    stack.pop()
                else:
                    stack.append(i)
        return stack==[]

if __name__=='__main__':
    print(Solution().isValid_1("[]"))