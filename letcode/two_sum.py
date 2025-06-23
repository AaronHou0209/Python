'''
Given an array of integers nums and an integer targer,
return indices of the rwo numbers such that they add up to target


Author: ChengYu Hou
Data: 18 April 2025

'''



def looking ():
    # ask user data
    nums = input("Enter your array :")
    target = int(input("which number you looking for ?"))

    # eval() could make str to list
    num_list = eval(nums)

    for i in range (0,len(num_list)):
        # prevent count from [:-1]
        if  i -1 >= 0 :
            first = num_list[i-1]
            second = num_list[i]
            cal = first + second
            print(cal)
        # match or not 
            if cal == target:
                 print([i-1, i])
            else:
                 print("Not Found")



# Best answer 
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# looking()