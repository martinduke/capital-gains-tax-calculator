import math

# This library computes the IRS tax table for tax year 2022. When the
# brackets change in later years, update "rate" and "min_at_rate" below
# accordingly.

# When you call this file directly, some tests run that spot-check based
# on the 2021 tax table.

def pure_tax_rate(income, status):
    # update these each year
    rate = [ .1, .12, .22, .24, .32, .35, .37 ]
    min_at_rate = [ [0, 10275, 41775, 89075, 170050, 215920, 539900],
                [0, 20550, 83550, 178150, 340100, 431900, 647850],
                [0, 10275, 41775, 89075, 170050, 215950, 323925],
                [0, 14650, 55900, 89050, 170050, 215950, 539900] ]
    i = 0;
    total = 0;
    while (i < len(rate) and min_at_rate[status][i] < income):
        incr = rate[i] * (income - min_at_rate[status][i])
        i = i+1
        if i < len(rate) and income > min_at_rate[status][i]:
            incr = rate[i-1] * (min_at_rate[status][i] - min_at_rate[status][i-1])
        total += incr
    return total

def tax(income, status):
    if (income < 5):
        return 0
    if (income < 15):
        return 1
    if (income < 25):
        return 2
    if (income >= 100000):
        return pure_tax_rate(income, status)
    if (income >= 3000):
        # $50 increments
        low = 50 * math.floor(income/50)
        high = 50 * math.ceil(income/50)
        if (low == high):
            high = low + 50
    else:
        low = 25 * math.floor(income/25)
        high = 25 * math.ceil(income/25)
        if (low == high):
            high = low + 25
    return round((pure_tax_rate(low, status) + pure_tax_rate(high, status))/2)

# Some tests to check vs. the tax table.
# format [income, status(0..3), expected tax]
test_array = [
    [1, 3, 0],
    [33, 2, 4],
    [1701, 0, 171],
    [18549, 2, 2024],
    [26700, 0, 3008],
    [42700, 1, 4729],
    [60947, 1, 6913],
    [88950, 0, 15375],
]
for test_case in test_array:
    if (tax(test_case[0], test_case[1]) != test_case[2]):
        print("test case " + str(test_case[0]) + ", " + str(test_case[1]) + " failed")
        print("  " + str(tax(test_case[0], test_case[1])) + " should have been " + str(test_case[2]))
