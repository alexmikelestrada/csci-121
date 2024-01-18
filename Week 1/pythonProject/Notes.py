import math
import random


def main():
                        print('hello my name is alex estrada')
                        print('There are things that my friends say like \"swag"')
                        # how to get quotes in lines
                        print('The old Crib\n100 riverside dr \nMagnolia DE 19962')
                        # how to separate lines with \n
                        person = 'Gaelon'
                        city = 'dover'
                        city2 = "wilmington"
                        print(person, "used to live in", city)
                        # using variables with assigned values
                        print(person, "used to live in", city, "now he lives in", city2)
                        person = 'nico'
                        city = 'magnolia'
                        print(person, "lives in", city)
                        person = 'gaelon'
                        city = 'wilmington'
                        print(person, "lives in", city)
                        person = 'madison'
                        city = 'milford'
                        print(person, "lives in", city)
                        # the line of code stays the same, but we change the variable to influence the output
                        print(2+2)
                        print(2.0+2)
                        # floats are numbers with decimal points, numbers mixed with floats will produce floats
                        print(10/2)
                        # division involving integers will always produce floats
                        print(20//4)
                        # use // to produce integer from division
                        print(19//4)
                        # answer is 4.75 but since we use // it throws the decimal point away without rounding'
                        print(1000/91)
                        print(1000//91)
                        print(20 % 4)
                        # modulo division, gives the remainder
                        # in PEMDAS there is levels of importance: P(parenthesis),E(**),MD(*, /, //, %),A(+),S(-)
                        print(2**3)
                        # use "**" to represent the ^ symbol when using exponents
                        print(25**0.5)
                        # raising number to a fractional exponent
                        print(27**(1/3))
                        print(64**(1/3))
                        # often when using floats the computer will never give you the exact answer
                        print(4**(-1))
                        feet = 5
                        inches = 12*feet
                        print('there are', inches, 'inches in', feet, 'feet')
                        # applying variables with multiplication
                        feet = 176
                        inches = 12*feet
                        print('there are', inches, 'inches in', feet, 'feet')
                        day = 365
                        hours = 24*day
                        minutes = 60*hours
                        seconds = 60*minutes
                        print('there are', seconds, 'seconds in', day, 'days')
                        print('there are', hours, 'hours in', day, 'days')
                        print('5 feet 3 inches =', 5+3/12, 'feet')
                        feet = 7
                        inches = 6
                        converted = feet+inches/12
                        print(feet, 'feet', inches, 'inches =', converted, 'feet')
                        # ^ line is more sophisticated as it has fewer variables to change
                        '''
                        This is a block comment
                        It uses three quote symbols to make the following lines comments
                        To close the comment you end the next line with 3 more quotations
                        '''


if __name__ == "__main__":
      main()


# syntax in programming is the rules of the language that you are using, the combinations allowed within the language
mylist = ("Rock", "Paper", 'Scissors')
print(random.choice(mylist))
apple_count = 140
basket_size = 12
print(apple_count, 'apples can be used to create',
      apple_count // basket_size, 'fruit baskets')
print(apple_count % basket_size, "apples will be left over")
# This code represents the use of modulo division
'''
username = ""
username = input("enter username")
print("username is " + username)
'''
total_inches = 85
feet = total_inches // 12
inches = total_inches % 12
print(total_inches, "inches =", feet, "feet", inches, "inches")
weeks = 4
days = 3
hours = 7
total_hours = hours + 24 * (days + weeks * 7)
print(weeks, "weeks", days, "days", hours, "hours is", total_hours, "hours")
x = 7
y = 9
print(f"{x+y} hello {x} {y} my name is alex ")
# (+=),(-=),(*=),(%=0,(/=),(//=), these are shorthand expressions
# they are used in variable manipulation
# x -= y is equal to x = x - y
print(-3 // -2)
width = 7
height = 9
area = width * height
print(f'the area of a rectangle with width={width} and height={height} is {area}')
# width = 8ft 6in
# height = 5ft 3 in
width_ft = 7
width_in = 3
height_ft = 10
height_in = 2
INCH_PER_FOOT = 12
width_total_in = INCH_PER_FOOT * width_ft + width_in
height_total_in = INCH_PER_FOOT * height_ft + height_in
width_total_ft = width_ft + width_in / INCH_PER_FOOT
height_total_ft = height_ft + height_in / INCH_PER_FOOT
area_sqin = width_total_in * height_total_in
area_sqft = width_total_ft * height_total_ft
print(f'width = {width_ft} ft {width_in} in')
print(f' height = {height_ft} ft {height_in} in')
print(f' area = {area_sqin} sq in')
print(f' area = {area_sqft} sq ft')
# find page 8 of the notes to learn more about constants
a, b, c = 12, 5, 4
print(f' {a} {b} {c}')
print(f' {a:5} {b}')
# 4321 seconds equals, hrs, min, seconds
seconds = 4321
minutes = seconds // 60
hours = minutes // 60
leftover_minutes = seconds % 60
print(hours)
print(minutes)
print(seconds)
print(leftover_minutes)
x = 'hot'
y = 'dog'
print(f' {x + y}')
print(f' {(x + y)*3}')


# Tuesday, October 3rd
def cube(z):
    return z ** 3


print(cube(2))
print(cube(0))
print(cube(1))
print(cube(10))
print(cube(-3))
print(f' the cube of 7 is {cube(7)}')


def sum(x, y):
    return x + y


def square(x):
    return x*x


print(f'4 + 5 = {sum(4, 5)}')
print( sum(sum(4,  5), 10))
print(sum(square(2), square(3)))


def greet(name):
    print(f'Hello {name}! Its nice to meet you!')


greet('Alex')
greet('Nico')
greet('Gaelon')


def areaOfRectangle(w, h):
    return w*h


def perimeterOfRectangle(w, h):
    return 2*(w+h)


w, h = 4, 5

print(f'width      = {w}')
print(f'height     = {h}')
print(f'area       = {areaOfRectangle(w,h)}')
print(f'perimeter  = {perimeterOfRectangle(w,h)}')


def hypotenuse(a, b):
    s = a*a + b*b
    c = s ** (1/2)
    return c


print(f'the hypotenuse is {hypotenuse(3, 4)}')


def hypotenuse_alt(a, b):
    return (a*a + b*b) ** (1/2)


def areaoftriangle(a, b):
    return (a*b/2)


def perimeteroftriangle(a, b):
    c = hypotenuse(a, b)
    return a + b + c


print(f'the hypotenuse is {hypotenuse(3,4)}')
print(f'the area is {areaoftriangle(3, 4)}')
print(f'the perimeter is {perimeteroftriangle(3, 4)}')

for i in [2, 50, 6, 7]:
    print(f' the square of {i} is {i*i}.')
def main_2():

    # Monday 23 October 2023
    num = int(input(f' pick a positive number'))
    print(num)
    if num % 2 == 0:
        print(f'the number {num} is even')
    else:
        print(f' the number {num} is odd')

    if num % 10 == 0:
        print(num)
    else:
        print(f'{num//10*10+10}')
        num_2 = num//10*10+10
    print(f' the next highest multiple of 10 for {num} is {num_2}')
    '''
    Above is showing how you can manipulate user inputs
    We can have the user input change in to any given parameter
    '''
    coi = int(input(f' pick a positive integer'))
    if coi % 2 == 0:
        print(f'the number {coi} is even')
    else:
        print(f'{coi+1}, this is the next even number')

    a = int(input(f'give me an integer: '))
    b = int(input(f'give me another integer: '))
    if a > b:
        print(f'{a} is bigger than {b}')
    else:
        print(f'{b} is bigger than {a}')

    a = int(input(f'give me a positive integer: '))
    b = int(input(f'give me another positive integer: '))
    c = int(input(f'give me one more positive integer: '))
    if a > b > c:
        print(f'{a} is the biggest number')
    if b > a > c:
        print(f'{b} is the biggest number')
    else:
        print(f'{c} is the biggest number')



if __name__ == "__main_2__":
      main_2()



# Monday 30 October 2023
# List slicing

x = ['apple', 'orange', 'coconut', 'banana', 'kiwi']
print(x)
print(x[1:3])
x = ['alex', 'nico', 'gaelon']
print(x)
x.append('mike')
print(x)
# adding an item to a list using append
x.insert(1, 'karaline')
print(x)
# adding an item into a particular spot using insert

# Thursday 2 November 2023
# didn't do anything :)
# Tuesday 7 November 2023
for i in [3, 4, 5, "cat", 4<7]:
    print(i)
for x in [3, 4, 5, 6, -1]:
    print(f' {x}     {x+x}       {100*x}')
# for x(can be any variable) then provide a list and then indented give the things you want to do to the list
for n in ['Alex', 'Gaelon', 'Nico', 'Karaline', 'Oscar']:
    print(f' hello! {n}, your name has {len(n)} letters in it!')
sum = 0
for s in [2, 3, 4]:
    sum = sum + s
    print(sum)
print(f' FORTNITE FORTNITE FORTNITE FORTNITE FORTNITE FORTNITE')
sum = 0
for o in [2, 3, 5, 7, 8, 9,]:
    if o % 2 == 1:
        sum = sum + o
        print(sum)
# Thursday 9 November 2023


def sill(a:str) -> int:
    if a.startswith('e'):
        print(500)
    else:
        print(1337)


def largest(x: list[int]) ->int:
    max = 0
    for n in x:
        if n > max:
            max = n
    return max


def smallest(x: list[int]) -> int:
    min = 999
    for n in x:
        if n < min:
            min = n
    return min


print(largest([4, 6, 7, 8, 9, 0, 12, 124, 14, 5, 35]))
print(smallest([4, 6, 7, 8, 9, 0, 12, 124, 14, 5, 35]))

# Tuesday 14 November 2023
print('break')
def smallest(x: list[int]):
    min = 1000
    for n in x:
        if n < min:
            min = n
    return min


print(smallest([4, 5, 12, 12356, 16, 34, 14]))
print(largest([2, 4, 2, 14, 15614, 123, 23]))

'''
QUESTION 7
age= (1, ..., 15) $12 (16, ..., 60)$25, (61,INF)
if it is a member, give them 15% off
if they use code "fun" then they get $3.50 of their fee
calculate the fee in 3 steps 
'''

# you want to spray paint a circle


def quest_8(radius: float, coverage: float) -> int:
    area = math.pi * radius ** 2

    return math.ceil(area / coverage)


def quest_10(x: str) -> str:
    if len(x) % 2 == 0:
        return x[0] + x[-1]
    else:
        middle = len(x) // 2
        return x[0] + x[middle] + x[-1]

# Thursday 16 November 2023


fruits = ('apple', 'banana', 'orange')
print(fruits[1])
for x in fruits:
    print(x)
print(f'fruits has {len(fruits)} items in it')
# tuples cannot be changed

x = ['apple', 'banana', 'carrot', 'soup']
print(len(x))

# Tuesday 21 November 2023
Decimal = 0.00
rounded = 0.00
n = 22
if n % 5 == 0:
    print(n)
else:
    decimal = n / 5
    decimal = math.ceil(decimal)
    rounded = decimal * 5
    print(rounded)

# Wednesday 29 November 2023

def sumofcubesevens(a:int, b:int) ->int:

ans = 0
for n in range(a, b + 1):
    if n % 2 == 0:
        ans += n ** 3
    return ans
