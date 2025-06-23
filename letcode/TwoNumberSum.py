"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
pp                                                                                                                            v  Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



"""



class Solution:
    def TwoList(self, l1, l2):
        l1_number = 0
        l2_number = 0
        final_number = 0
        for i in range(len(l1) -1 ,-1,-1):
            l1_number += l1[i] * (10 ** (i))

        for y in range(len(l2) -1,-1,-1):
            l2_number += l2[y] * (10 ** (y))
        final_number = (l1_number + l2_number)


        return [ int(d) for d in str(final_number)][::-1]




s1 = Solution()

c1 = s1.TwoList([2,4,3], [5,6,4])

print(c1)