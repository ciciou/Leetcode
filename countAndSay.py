#-*-coding: utf-8 -*-
#author:cici
class CountandSay:
    def countAndSay(self, n: int) -> str:
        """
        Runtime: 48ms、 Memory: 13.1MB
        思路： 暴力
        """
        if n == 1:
            return "1"
        result = "1."
        for i in range(1, n):
            count = 1
            temp = ""
            for index in range(1, len(result)):
                if result[index] \
                        == result[index - 1]:
                    count += 1
                else:
                    temp = f"{temp}{count}{result[index - 1]}"
                    count = 1
            result = f"{temp}."
        return result[:-1]


if __name__ == "__main__":
    print(CountandSay().countAndSay(6))