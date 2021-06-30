

# print(1/0) #ZeroDivisionError: division by zero
#
# num = 9
# if num > 8: # this would throw syntax error SyntaxError: invalid syntax
#     print(num)

# we will create a file with required permission and see what errors/exception are possible to be seen
# first iteration
# file = open("order.text") # open() takes a string arg with file name
# print(file) # Let's see the outcome and record it

# # second iteration
# try:
#     file = open("order.text")
#     print("file found") # try block required except or will throw an error
#
# except FileNotFoundError as errmsg: # creating alias same as a nick name
#     print(f"file not found {errmsg}")
#
# finally: # Finally will execute regardless of try and except block execution, also used to clean up the code
#     print("Thank you for visiting See you again!")

# Let's create a file called order.text - naming is essential so ensure it has the same name as above

# Let's apply DRY - OOP - Python Packaging
           #   1     2         3
#
# # 3rd Iteration
# # Create a function to the same job DRY

def open_using_with_and_print(file): # takes one string arg
    try:
        with open(file, "r") as file: # file with read permission
            for line in file.readlines(): # iterating through data from the file with readlines()
                print(line.rstrip('\n')) # strinpping and printing data in each line

    except FileNotFoundError:
        print("file cannot be found or directory is incorrect, please check the details provided")
        raise

    finally:
        print("\nPlease chose the items from the list  and enjoy your HAPPY MEAL")

open_using_with_and_print("order.text") # calling the function











# fourth iteration
# add desert and Ice cream to orders.text

# def write_to_file(file, order_item): # function to add items into the file
#     try:
#         with open(file, "w") as file: # file with write permission
#             file.write(order_item + '\n') # adding an item
#     except FileNotFoundError:
#         print("file cannot be found or directory is incorrect, please check the details provided")
#         raise
#
# write_to_file("order.text", "Ice Cream") # calling function and pass item name to be added to the order.text

