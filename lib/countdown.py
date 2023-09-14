# your code goes here!
import time

def countdown(n):
    while n > 0:
        print(f"{n} SECOND(S)!")
        n -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(n):
    while n > 0:
        print(f"{n} SECOND(S)!")
        n -= 1
        time.sleep(1)  # Sleep for one second between iterations
    print("HAPPY NEW YEAR!")
    
