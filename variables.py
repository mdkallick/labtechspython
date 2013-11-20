## Written by Mathias Dyssegaard Kallick 10/13/13
## Intro to variables and their uses.

# Variables, in coding, are very similar to variables in math. They are words or letters that you can assign numbers or words to, and possibly change the assigned word or number.
# For example:
x = "hello world"
# will set the variable x as being the two words "hello world." This can be very helpful, especially if you want to use those words more than once. By doing this, I could do the command:
print "hello world"
# in much less time simply by typing
print x
# which will simply print whatever value is assigned to x. If you run this script, you will see "hello world" printed twice: once from the first command, and once from the second.

# Variables can also be used to do math, or, as you'll see later, run while loops for a certain number of iterations. for example;
y = 10
z = 5
# will set y to the numerical value 10, and z to the numerical value 5. Therefore:
print y - z
# will print the value of 10 - 5: 5.
# I could also reassign x to this value:
x = y - z
# And running:
print x
# will also print that value: 5.
# Notice that x is no longer set as hello world, and is now 5, a number.

# Here's something really interesting: you can do addition and multiplication of strings, as well as numbers. For example:
print "Hi!" * 2
# Will print Hi!Hi! Also:
print "Hi!" + "Hello!"
# Will print Hi!Hello!. You can put spaces in the strings if you want.

# Variables are great, and they should be used as often as possible, to save time and make your code neater. Also, they will come in handy for writing loops. However, there are limitations: The name of the variable must start with a letter (it should anyway, as variables should be soemthing you can remember). Also, the variables must be either strings or numbers. This:
# x = hi
# Will not work.
