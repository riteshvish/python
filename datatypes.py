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

divided("Python Data Types Starts Here");
enter()
print "Numeric :"
print "int - long - float - complex"
a=100
b=1000000000000054641635
c=10.2345
d=100+3j
print a,"-",b,"-",c,"-",d
print type(a),"-",type(b),"-",type(c),"-",type(d)
enter()
print "String :"
a = "string in a double quote"
b= 'string in a single quote'
print(a)
print(b)
# using ',' to concate the two or several strings
print(a,"concated with",b)
#using '+' to concate the two or several strings
print(a+"concated with "+b)
enter()
print "List :"
#list of having only integers
a= [1,2,3,4,5,6]
print(a)
#list of having only strings
b=["hello","john","reese"]
print(b)
#list of having both integers and strings
c= ["hey","you",1,2,3,"go"]
print(c)
#index are 0 based. this will print a single character
print(c[1]) #this will print "you" in list c
enter()
print "Tuple :"

divided("Python Data Types Ends Here");
