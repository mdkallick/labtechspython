#Script to search files and determine whether a search key is found within them. Written by Mathias Kallick on 6/10/2013

linenumber = 0

searchedfile = raw_input('enter the full name of the file you want to search (example.txt): ')

filename = open('/media/mathias/pythonstuff/searchedfile', 'r')

input = raw_input('enter the text you want to search for: ') + '\n' # This line takes an input from the user : raw_input('text') will print text, and whatever you type in, it will set to the variable input.

while linenumber <= 200: # This is the first line of a while loop. It sets the parameters for when the loop will continue running and when it will stop running.
  
  textinfile = filename.readline() # This sets the variable textinfile to be the text in the current line of the file that is being read from. The linenumber is the same as the variable linenumber (see how you can name your variables nicely?)
  
  if textinfile == input: # This line compares the two variables input and textinfile. The if command will run anything that is indented under it if the statement after it (textinfile = input) is true, and will not run it if it is not true.
    print 'That input is a line in the file you are searching.'
    print 'that input is in the line: ' + linenumber
  
  linenumber = linenumber + 1 # This line is what continues the script, and eventually ends the script. Since a loop will continue from the first line, once the counter linenumber hits 200 (the final line in the file, and also the parameter that the while loop is told to stop by) the while loop will terminate, and the rest of the program will run.

raw_input('press enter to exit this script') # This line simply keeps the python shell open so you can see what the results are. Otherwise the shell will automatically close as soon as it runs out of commands to run.
