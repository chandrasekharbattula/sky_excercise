# Sky Coding Exercise 

## Problem Statement 

Each day at The Phone Company a batch job puts all the customer calls for the previous day into a single log file of:

```'customer id','phone number called','call duration'```

For a customer the cost of a call under 3 minutes is 0.05p/sec, over 3 minutes it is 0.03p/sec. However, there is a 
promotion on and the calls made to the phone number with the greatest total cost is removed from the customer's bill.

### Task
Write a program that when run will parse the calls.log file and print out the total cost of calls for the day for each 
customer. You can provide your solution in your preferred language (Python preferable)

calls.log :
```
A 555-333-212 00:02:03
A 555-433-242 00:06:41
A 555-433-242 00:01:03
B 555-333-212 00:01:20
A 555-333-212 00:01:10
A 555-663-111 00:02:09
A 555-333-212 00:04:28
B 555-334-789 00:00:03
A 555-663-111 00:02:03
B 555-334-789 00:00:53
B 555-971-219 00:09:51
B 555-333-212 00:02:03
B 555-333-212 00:04:31
B 555-334-789 00:01:59
```

## Solution

This solution makes use of pandas in python to determine the calls made to the phone no with the greatest total cost 
and then to calculate the total cost of the calls made by each customer for that day removing the calls made the phone
number determined previously.

#### How the phone no with the greatest total cost can be determined ? 
GroupBy on the phone no's, sum the cost of each call made to it, followed by sorting in descending order on total cost
and then take the phone no of the top row.

#### How the total call cost for each customer can be calculated ? 
Filter the call logs to exclude the phone no to with the greatest total cost from the list, then group by on customer 
id. Now, sum the cost of each call made which gives the result, total call cost for each customer on that day.