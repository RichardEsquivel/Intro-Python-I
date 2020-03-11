"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
# with open takes two commands by default it goes with r for read, can capture this return of data in a variable and print out
with open('foo.txt') as file:
    i_can_read = file.read()
    print(i_can_read, "\n")
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE the w commands writes to text
with open("bar.txt", "w") as file:
    file.write("Man text is fun! \n")
    file.write("Still super fun!!! \n")
    file.write("Getting less fun now.... \n")

# now will look at what we wrote by printing it out.
with open("bar.txt") as file:
    print(file.read())
