class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = 0
        temp = x
        while temp != 0:
            num = temp % 10
            temp = int(temp/10)
            a = a*10 + num
        if a == x:
            return True
        else:
            return False