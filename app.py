def print_hello():
    print("Hello from app")

# With dunder name == dunder main, the print_hello function will only run
# if the app.py file is called directly. Not when imported though.
if __name__ == '__main__':
    print_hello()