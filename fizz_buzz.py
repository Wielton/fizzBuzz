def fizzy():
    for num in nums:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print("This number isn't divisible by 3 or 5")

nums = [2,3,4,5,8,10,13,15,25,30,45,48,50,52,56,64,72]
print(fizzy())