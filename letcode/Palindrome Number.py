class Solution(object):

    def isPalindrome(self,x):
        x = str(x)
        print(x)
        if(x.startswith("-")):
           return "false"
        else:
            if ( int(x) == int(x[::-1])):
                print(x)
                return "true"
            elif (int(x) != int(x[::-1])):

                return "false"




solution = Solution()
solution.isPalindrome(121)
solution.isPalindrome(-121)
solution.isPalindrome(10)



