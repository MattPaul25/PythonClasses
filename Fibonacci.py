#Fibonacci function using a yield return

def FibonacciCounter(UpTo, predicate): #returns serious of numbers so long as they match predicate
    current, nxt = 1, 1
    if predicate(current):
        yield current

    while current <= UpTo: 
        current, nxt = nxt, current + nxt
        if predicate(current):
            yield current


#lambda n : n / 1 == n) # this lambda as predicate would always return true


someNums = Fibonacci(600, lambda n : n % 2 == 0) #just even numbers


for num in someNums:
    print(num)