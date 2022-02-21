import tax_table

# This file computes each line of the "Qualified Dividends and Capital
# Gain Tax Worksheet" for form 1040, Tax Year 2021.

# For future tax years, you should check this worksheet in the 1040
# instructions to make sure that the allowances listed on line 6 and line
# 13 are still accurately reflected in the arrays "l6_thresholds" and
# "l13_thresholds". These are listed in the order [Single, Married
# Filing Jointly, Married Filing Separately, and Head of Household].

def println(line, arg):
    print("Line " + str(line) + ": $" + ("{:10.2f}".format(arg)))

# These will probably change each year
l6_thresholds = [ 40400, 80800, 40400, 54100 ]
l13_thresholds = [ 445850, 501600, 250800,  473750]

print("Filing Status")
print("(1) Single")
print("(2) Married Filing Jointly")
print("(3) Married Filing Separately")
print("(4) Head of Household")

status_code = int(input("-> ")) - 1

print("")
l = []
l.append(2021)
l.append(float(input("1040 Line 15: ")))
l.append(float(input("1040 Line 3a: ")))
sched_d = input("Filed schedule D (y/n) ")
if sched_d == 'y' or sched_d == 'Y':
    d15 = float(input("1040, Schedule D, Line 15: "))
    d16 = float(input("1040, Schedule D, Line 16: "))
    l.append(min(d15, d16))
else:
    l.append(float(input("1040SR, Line 7: ")))

print("")
print("")
print("WORKSHEET OUTPUT:")
l.append(l[2] + l[3])
l.append(l[1]-l[4])
l.append(l6_thresholds[status_code])
l.append(min(l[1],l[6]))
l.append(min(l[5],l[7]))
l.append(l[7]-l[8])
l.append(min(l[1], l[4]))
l.append(l[9])
l.append(l[10]-l[11])
l.append(l13_thresholds[status_code])
l.append(min(l[1], l[13]))
l.append(l[5] + l[9])
l.append(l[14] - l[15])
l.append(min(l[12], l[16]))
l.append(l[17] * 0.15)
l.append(l[9] + l[17])
l.append(l[10] - l[19])
l.append(l[20] * 0.2)
l.append(tax_table.tax(l[5], status_code))
l.append(l[18] + l[21] + l[22])
l.append(tax_table.tax(l[1], status_code))
l.append(min(l[23], l[24]))

i = 0
for line in l:
  if (i > 0):
      println(i, l[i])
  i = i + 1
print("Copy line 25 to line 16 of Form 1040 or 1040-SR")
