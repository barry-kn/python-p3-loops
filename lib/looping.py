 #####  happy_new_year
####  pseudo code 
### >>> count down 
### while countdown is greater then 1 
### output value of countdown 
###  toa 1 from coutdown then at last happynew .......
     
def happy_new_year():
    countdown = 10
    
    while countdown > 1:
        print(countdown)
        countdown -= 2
    
    print("Happy New Year")

happy_new_year()


def square_integers(nums):
    squared_nums = []
    
    for num in nums:
        squared_nums.append(num ** 2)
    
    return squared_nums

result = square_integers([1, 2, 3, 4, 5])
print(result)

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz()
