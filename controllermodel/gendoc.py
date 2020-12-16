
# I would've liked to use pdoc for this task, but pdoc is unfortunately
# too tailored to actual class documentation, and not API documentation,
# which isn't a bad thing! It just means we must do more heavy lifting
# ourselves, which is ok! We can borrow concepts and methods from pdoc
# to help us along in our implementation.

# To note, the main reason we can't use pdoc is because pdoc wants to 
# generate documentation for python classes and modules, whereas we
# simply want to generate documentation for our special controllers.

class GenDoc:
    pass