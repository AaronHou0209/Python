
class Solution(object):
    def intToRoman(self, num):
        #  how many 1000
        m = int(num / 1000)
        # delete above 1000
        under_thousand = num - 1000 * m
        # how many 500
        d = int(under_thousand /500 )
        # Beside 500
        beside_FiveHoundred = under_thousand - 500 *d
        # how many 100
        c = int (beside_FiveHoundred / 100)
        # Beside 100
        beside_houndred = beside_FiveHoundred - c *100
        # how many 50
        l = int(beside_houndred / 50)
        # Beside 50
        beside_Fifty = beside_houndred - l * 50
        # how many 10
        x = int(beside_Fifty / 10)
        # Beside 10
        delete_10 = beside_Fifty - x * 10
        # how many 5
        v = int(delete_10 / 5)
        # beside 5
        delete_5 = delete_10 - v * 5
        # how many 1
        i = int(delete_5 / 1)

        Mtimes = "M" * m
        DTimes = "D" * d
        CTimes = "C" * c
        LTimes = "L" * l
        XTimes = "X" * x
        VTimes = "V" * v
        ITime = "I" * i
        return f"{Mtimes}{DTimes}{CTimes}{LTimes}{XTimes}{VTimes}{ITime}"


solution = Solution()
print(solution.intToRoman(3749))
print(solution.intToRoman(58))
print(solution.intToRoman(1994))

