import os
os.system('clear')

print("""
 _______  __   __  _______  __   __  _______  __    _
|    _  ||  |_|  ||_     _||  |_|  ||   _   ||   |_| |
|    ___||_     _|  |   |  |       ||  |_|  ||  _    |
|___|      |___|    |___|  |__| |__||_______||_|  |__|

""")

# helpers
def divided(msg=""):
    print """
==================="""+msg+ """==========================
"""

def enter(msg=""):
    print "\n"

divided("Python Loops Starts Here");

# Prints out the numbers 0,1,2,3,4
# for x in range(5):
#     print(x)
# enter()
#
# # print all numbers Starts from 3 till lessthen 6
# # Prints out 3,4,5
# for x in range(3, 6):
#     print(x)
# enter()
#
# # print all second numbers Starts from 3 till lessthen 8
# # Prints out 3,5,7
# for x in range(3, 8, 2):
#     print(x)

number=40
for j in range(1,number):
    if j < number/4*1 :
        print((number-j)*" "+j*" *")
    elif j < number/4*2:
        print(j*" "+(number-j)*" *")
    elif j < number/4*3 :
        print((number-j)*" "+j*" *")
    else :
        print(j*" "+(number-j)*" *")
enter()


# count = 0
# while count < 5:
#     print count,
#     count += 1  # This is the same as count = count + 1
# enter()
# count = 0
# while True:
#     print count,
#     count += 1
#     if count >= 5:
#         break
#
#
# enter()
# # Prints out only odd numbers - 1,3,5,7,9
# for x in range(10):
#     # Check if x is even
#     if x % 2 == 0:
#         continue
#     print(x)
#
#
# enter()
# # Prints out only odd numbers - 1,3,5,7,9
# for x in range(10):
#     # Check if x is even
#     if x % 2 == 0:
#         print x, " odd numbers"
#     else :
#         print x, " even numbers"



divided("Python Loops Ends Here");
