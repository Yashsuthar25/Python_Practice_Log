# let's explore how to create functions in python and also some basic inbuilt functions.

def area_triangle(base, height):
    return base * height /2

area_1 = area_triangle(2, 4)
area_2 = area_triangle(3, 5)
area_3 = area_1 + area_2
print(area_2)

def get_price(producing_cost, profit_share):
    return producing_cost + profit_share

product_1 = get_price(12, 8)
print(product_1)
# Sorry, I'm not currently able to think of a function that I can create, once I do, I'll make some
#useful functions.

# this defines discount for different people separately.
name = 'Yash'
number = len(name)
print("Hello " + name + ", You have won " + str(number) + " percent discount on your purchase at Atoms")

name = 'Yuvraj'
number = len(name)
print("Hello " + name + ", You have won " + str(number) + " percent discount on your purchase at Atoms")

#now, let's make this above code more accessible.
def lucky_customer(name):
    number = len(name)
    print("Hello " + name + ", You have won " + str(number) + " percent discount on your purchase at Atoms")

lucky_customer("VaibhavSuryavanshi")

#Just this much for today, I'll increase the time pace with my understanding.
# Sorry, but I'm working on something else today, so NO SQL FOR TODAY.