#!/usr/bin/python3
def fizzbuzz():
    for i in range(101):
        if (i % 3 and i % 5):
            print(f"{'FizzBuzz':1s}", end="")
        elif (i % 3):
            print(f"{'Fizz':1s}", end="")
        elif (i % 5):
            print(f"{'Buzz':1s}", end="")
        else:
            print(f"{i:1s}", end="")
