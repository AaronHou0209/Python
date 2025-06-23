"""
Editor: ChengYu Hou

Date: 2 Feb 2025

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""
class Solution(object):
    def __init__ (self, l1, l2):
        if l1[0] == 0 and len(l1) == 1:
            self.l1 = l1
            if l2[0] == 0 and len(l2) == 1:
                l2.reverse()
                self.l2 = l2
            elif l2[0] != 0:
                l2.reverse()
                self.l2 = l2
        elif l1[0] != 0 :
            self.l1 = l1
            if l2[0] == 0 and len(l2) == 1:
                l2.reverse()
                self.l2 = l2
            elif l2[0] != 0:
                l2.reverse()
                self.l2 = l2


    def sumNumbers(self):

        stringnumber1 = "".join(map(str, self.l1))
        stringnumber2 = "".join(map(str, self.l2))
        number1 = int(stringnumber1)
        number2 = int(stringnumber2)
        total_sum = number1 + number2
        return total_sum


    def sum_to_list(self):
        return  list(str(self.sumNumbers()))[::-1]


#Main Code
example1 = Solution(l1 = [0], l2 = [0])
finalAnswer = example1.sumNumbers()
print(finalAnswer)

sum_as_list = example1.sum_to_list()
print(sum_as_list)