''' Hello, it was a short break, now I'll continue with some basic functions for now, I'll increase my session time as
  I learn more. '''

def total_sales(price, quantity):
    return round(price * quantity, 2)

total_sales_2026_08_01 = total_sales(17.99, 34)
print(total_sales_2026_08_01)

name = 'Yash Suthar'
split_name = name.split()
print(split_name)
# this would seem pretty basic, but it is useful and I'm trying to just create the habit just like I di with MySQL.

marks_list = [34, 56, 78, 90, 12, 45]
def average_marks(marks):
    return sum(marks)/len(marks)

print(average_marks(marks_list))

def max_marks(marks):
    return max(marks)

print(max_marks(marks_list))
# let's end this here, I'll come up with new things in python soon, and I'll try to make it more useful and practical for me.

