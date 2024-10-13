# Atabek Kubanychbek uulu
# 10/12/24
# Assignment 3

# Remember to comment for each function

# This method prints "Hello World"
def print_hello():
    # TODO: Print "Hello World"
    print('Hello World')

# This method print "Hello, " and name given in the arguments
def hello_user(name):
    # TODO: Print "Hello, their_name"
    print(f'Hello, {name}')

#This method prints circle area of given radius
def get_circle_area(radius):
    # TODO: print a message back with the answer
    print(math.pi * radius **2)

# This method gives MPG of given miles and gallons in the arguments
def get_miles_per_galoon(miles, gallons):
    # TODO: print out the MPG for the car
    mpg = miles/gallons
    print(f'MPG: {mpg}')
    
# This method returns converted farenheit into celcius
def convert_temperature(temperature_F):
    # TODO: return the coverted temperature in Celcius
    return (temperature_F-32)*5/9

# I am not sure about this method's instructions, 
# however, this method here does return new day of the week

def problem_7(starting_day, length_of_stay):
    # TODO: Implement the function as the problem statement
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    
    day_of_stay = (starting_day+length_of_stay)%7
    return days_of_week[day_of_stay]

#This method prints all leap years from 1900 to 2100
def extra_credit_problem_1():
    start_year = 1900
    end_year = 2100
    # TODO: Write a program to print leap years from the year 1900 to 2100
    # 5 points extra credits
    for i in range(start_year, end_year+1):
        if (i%4==0):
            if (i%100==0):
                if(i%400==0):
                    print(i)
            else:
                print(i)

#This method checks if N is a prime number
def extra_credit_problem_2(n):
    # a prime number is a natural number greater than 1, that can only divisible by itself and 1
    # 10 points extra credits
    # TODO: given the number n, check if n is a prime number

    # We already know that prime number should be devisible by two numbers (1, and N itself). 
    # So I am checking divisibility of any numbers besides 1 and N itself which in case "true" makes N not primary
    prime_number = "PRIME NUMBER"
    if(n<2):
        prime_number = "NOT PRIME NUMBER"
    elif(n>2):
        for i in range(2, n-1):
            if(n%i==0):
                prime_number = "NOT PRIME NUMBER"
                break
    
    
    return prime_number


def main():
    print_hello()
    hello_user('Ata')
    get_circle_area(3)
    get_miles_per_galoon(6,2)
    print(convert_temperature(83))
    print(problem_7(2,6))
    extra_credit_problem_1()
    print(extra_credit_problem_2(5))
    # prompt user to get the input then call functions
    # ...
    
main()


    


