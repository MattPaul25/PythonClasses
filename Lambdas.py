# the yield value of returns i when the predicate of i = true
# predicates can take lambda expression that yields a true or false
# returns the values that are true according to the lambda expression


def find_numbers(predicate):
    for i in range(0 ,100):
        if predicate(i):
            yield i


#lambda n : (n / 3) > 14)
# is like saying: where n / 3 is greater than 14


some_nums = find_numbers(lambda n : n % 5 == 1) 

for num in some_nums:
    print(str(num), end = ', ') # prints all values in number (end replaces the new line arg)