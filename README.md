# Working with Files
## Exception handling
### File permissions

##### Example of errors/exception
-  `value error`
- `syntax error`
- `out of bounce `
- `key error`
- `attribute error`
- `ZeroDivisionError: division by zero`

##### File permissions

- `r` This is the default mode. It opens file for reading
- `w` This mode opens file for writing. If file doesn't exist, it creates a new file for us
- `x` Creates a new file, if already exists, the operation fails
- `a` Opens file in Append Mode, if file doesn't exist, it creates a new one
- `t` This the default mode to open in text mode
- `b` This for binary mode
- `+` This will open a file for reading and writing (updating) 

**we have `try` `except` and `finally`**
- `try` works as `if condition`
- `except` works as `elif`
- `finally` works as else, finally will execute regardless of `try` and `except` conditions  

# Let's see these in action
```python
file = open("order.text") # Looks for the file called order.text
print(file)
#run program

# first iteration - using exception handling
try:
    file = open("order.text")
    print("file is found")
except:
    print("file not found")

# second iteration with capturing error message
try:
    file = open("order.text")
    print("file found ")
except FileNotFoundError as errmsg: # add alias
    print(f"The above block of code was not executed as {errmsg} found ")
finally:
    print("Thank you visiting")

# Apply DRY
def open_using_with_and_print(file):
    try:
        with open(file, "r") as file:
            for line in file.readlines():
                print(line.strip('\n'))
    except FileNotFoundError:
        print("file can't be found please check the name")
        #raise
    finally:
        print("\nPlease choose the items from the list and enjoy your HAPPY MEAL")

open_using_with_and_print("order.text")
```

```python

def write_to_file(file, order_item):
    try:
        with open(file, "w") as file: # the `w` has the functionality abstracted
            file.write(order_item + '\n')
    except FileNotFoundError:
        print("file cannot be found or directory is incorrect, please check the details provided")
        raise

write_to_file("food.text", "apple")

```