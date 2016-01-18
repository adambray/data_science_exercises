'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''
import csv
with open('orders.tsv','rU') as f:
    file_data = [row for row in csv.reader(f, delimiter='\t')]



'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''
header = file_data[0]
data = file_data[1:]


'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''

'''
# Here I was just playing with default dict to learn how it worked.

import collections
order_prices = collections.defaultdict(int)
for row in data:
    order_num = int(row[0])
    item_price = float(row[4][1:])
    order_prices[order_num] += item_price
    
order_prices

num_orders = len(order_prices)

total_price = 0
for order_id, price in order_prices.iteritems():
    total_price += price
    
averave_price_per_order = total_price / num_orders
'''


order_ids = [int(row[0]) for row in data]
order_ids = set(order_ids) # convert list to set to grab unique order ids

num_orders = len(order_ids)

total_price = 0
for row in data:
    item_price = float(row[4][1:]) 
    total_price += item_price

averave_price_per_order = total_price / num_orders

print round(averave_price_per_order, 2)


'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''
soft_drink_items = [row[3] for row in data if ("Canned" in row[2])]
soft_drink_items = [item.strip('[]') for item in soft_drink_items]

soft_drinks = set(soft_drink_items)


'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''

burrito_items = [row for row in data if ("Burrito" in row[2])]

toppings = 0
for item in burrito_items:
    # add one because we're only counting commas, and we need to count the 
    # last item in the list too. Using count to avoid making an array if we 
    # used 'split'
    num_toppings = item[3].count(',') + 1 
    toppings += num_toppings
    
avg_burrito_toppings = toppings / float(len(burrito_items))

print "Burrito Toppings: ", round(avg_burrito_toppings, 2)


'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''

chip_items = [row for row in data if ("Chip" in row[2])]

# clean up data to make 'Chips' and 'Side of Chips' the same, and to normalize
# salsa names (hyphens and variants in name)
for item in chip_items:
    item[2] = item[2].replace("-", " ")
    if item[2] == 'Chips':
        item[2] = 'Side of Chips'
    if item[2] == 'Chips and Mild Fresh Tomato Salsa':
        item[2] = 'Chips and Fresh Tomato Salsa'


import collections
chip_orders = collections.defaultdict(int)

for item in chip_items:
    name = item[2]
    qty = int(item[1])
    chip_orders[name] += qty

chip_orders

'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''

'''
QUESTION: Is there any difference in avg number of toppings between bowls, 
burritos, and main protien?
'''

def get_avg_toppings(data, match_string):
    items = [row for row in data if (match_string in row[2])]
    
    toppings = 0
    for item in items:
        # add one because we're only counting commas, and we need to count the 
        # last item in the list too. Using count to avoid making an array if we 
        # used 'split'
        num_toppings = item[3].count(',') + 1 
        toppings += num_toppings
        
    return toppings / float(len(items))


print "Burrito Toppings: ", round(get_avg_toppings(data, "Burrito"), 2)
print "Bowl Toppings: ", round(get_avg_toppings(data, "Bowl"), 2)
print "Chicken Toppings: ", round(get_avg_toppings(data, "Chicken"), 2)
print "Steak Toppings: ", round(get_avg_toppings(data, "Steak"), 2)
print "Carnitas Toppings: ", round(get_avg_toppings(data, "Carnitas"), 2)
print "Barbacoa Toppings: ", round(get_avg_toppings(data, "Barbacoa"), 2)
print "Veggie Toppings: ", round(get_avg_toppings(data, "Veggie"), 2)
