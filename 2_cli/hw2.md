## Homework exercise - CLI

### Question 1

Look at the head and the tail, and think for a minute about how the data is structured. What do you think each column means? What do you think each row means? Tell me! (If you're unsure, look at more of the file contents.)

```
$ head chipotle.tsv
order_id	quantity	item_name	choice_description	item_price
```

Each row is an item in an order. Order_id is the id of the order it belongs to,
quantity is how many of that item, item_name is the item's name, choice_description
includes more info about that choice (toppings, type, etc), and item_price includes
the total price for that item (factoring in quantity)

### Question 2.

How many orders do there appear to be?

```
$ tail chipotle.tsv

1832	1	Chicken Soft Tacos	[Fresh Tomato Salsa, [Rice, Cheese, Sour Cream]]	$8.75
1832	1	Chips and Guacamole	NULL	$4.45
1833	1	Steak Burrito	[Fresh Tomato Salsa, [Rice, Black Beans, Sour Cream, Cheese, Lettuce, Guacamole]]	$11.75
1833	1	Steak Burrito	[Fresh Tomato Salsa, [Rice, Sour Cream, Cheese, Lettuce, Guacamole]]	$11.75
1834	1	Chicken Salad Bowl	[Fresh Tomato Salsa, [Fajita Vegetables, Pinto Beans, Guacamole, Lettuce]]	$11.25
1834	1	Chicken Salad Bowl	[Fresh Tomato Salsa, [Fajita Vegetables, Lettuce]]	$8.75
1834	1	Chicken Salad Bowl	[Fresh Tomato Salsa, [Fajita Vegetables, Pinto Beans, Lettuce]]	$8.75
```

Implies there are 1834 orders.


### Question 3

How many lines are in the file?

```
$  wc -l chipotle.tsv
    4623 chipotle.tsv
```

4623 lines

### Question 4

Which burrito is more popular, steak or chicken?

```
$  grep 'Steak Burrito' chipotle.tsv  | wc -l
     368
$  grep 'Chicken Burrito' chipotle.tsv  | wc -l
    553
```

Do chicken burritos more often have black beans or pinto beans?

```
$  grep 'Chicken Burrito' chipotle.tsv | grep 'Pinto Beans'  | wc -l
  105
$  grep 'Chicken Burrito' chipotle.tsv | grep 'Black Beans'  | wc -l
  282
```

Black Beans

### Question 5

Make a list of all of the CSV or TSV files in the DAT7 repo (using a single command). Think about how wildcard characters can help you with this task.

```
$  find . -name "*.?sv"
```

### Question 6

Count the number of occurrences of the word 'dictionary' (regardless of case) across all files in the DAT7 repo.

```
$  grep -ri 'dictionary' .
```

### Question 7

Optional: Use the the command line to discover something "interesting" about the Chipotle data. The advanced commands below may be helpful to you!
