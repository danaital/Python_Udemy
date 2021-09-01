# True
# False
# i= int(input("enter a int"))
# if 4<=i<=10:
#     print("OK")
# else:
#     print("OK1")


# coding ex6
# x= 5
# y= 7
# if x!=y:
#     if x>y:
#         print("x is bigger than y")
#     else:
#         print("x is smaller than y")
# else:
#     print("x equals y")


# Challenge 1
# name = input("Please enter a name")
# age = int(input("Hi {0}, please enter your age".format(name)))
# if 18<=age<31:
#     print("{}, you are more than welcome to join the holiday".format(name))
# else:
#     print("Sorry {}, you may not join the holiday".format(name))


# coding ex7
# for i in range (0,10):
#     print("{}".format(i))

# coding ex8
# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """
#
#
# for char in quote:
#     if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         print (char)


# coding ex9
# for i in range(0,101):
#     if i%7==0:
#         print(i)
#
# for i in range(0,101,7):
#     print(i)

# coding ex10
# for i in range(0, 100, 7):
#     print(i)
#     if i%11==0 and i>0:
#         break

# coding ex11
# for i in range (0,21):
#     if (i%3==0) or (i%5==0):
#         continue
#     else:
#         print(i)
# # without continue
# for x in range(20):
#     if x % 3 != 0 and x % 5 != 0:
#         print(x)

# coding ex12
# number = 5
# multiplier = 8
# answer = 0
# for i in range (multiplier):
#     answer +=number
#
# print(answer)

# Challenge 2
# ipAddress = input("Please enter IP address: ")
# segment = 1
# segmentLength = 0
# character = ''
# for character in ipAddress:
#     if character == '.':
#         print("segment {} contain {} ".format(segment, segmentLength))
#         segment += 1
#         segmentLength = 0
#     else:
#         segmentLength += 1
# if character != '.':
#     print("segment {} contain {} ".format(segment, segmentLength))


# Challenge 3
import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))
guess = int(input())
counter = 1
lastString = ""
while guess != answer:
    if guess == 0:
        print("GAME OVER\n YOU LOSE")
        break
    if guess > answer:
        print("Wrong number, please choose a lower number")
    else:
        # a lower number
        print("Wrong number, please choose a higher number")
    counter += 1
    print("Please guess a number between 1 and {}".format(highest))
    guess = int(input())
else:
    if counter == 1:
        lastString = "first"
    elif counter == 2:
        lastString = "second"
    elif counter == 3:
        lastString = "third"
    else:
        lastString = str(counter) + "th"
    print("You have guessed correctly the answer is {}. you got it on the {} try".format(answer, lastString))
