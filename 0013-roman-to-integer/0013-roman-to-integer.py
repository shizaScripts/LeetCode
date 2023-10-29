class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        arr=[]
        for i in range(len(s)):
            if s[i] == "I":
               temp = 1
            elif s[i] == "V":
                temp = 5
            elif s[i] == "X":
                temp = 10
            elif s[i] == "L":
                temp = 50
            elif s[i] == "C":
                temp = 100
            elif s[i] == "D":
                temp = 500
            elif s[i] == "M":
                temp = 1000
            arr.append(temp)

        for i in range(len(arr)):
            if i < len(arr)-1:
                print("less",i)
                if arr[i] >= arr[i+1]:
                    num += arr[i]
                else:
                    num -= arr[i]
            else:
                num += arr[i]

        return num
