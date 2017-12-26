# indentation
for i in range(1, 12):
    print(i)  # Python does not use delimeters but just uses and expects indents at least one
    print(i // 2)  # we can continue after indents to continue inside the block
    # we can also add more complex codes here inside the block as well
    if (i % 2) == 0:
        print("{} is an even number".format(i))
# above settings by selecting Code, navigate to reformat code to clean up the code structure