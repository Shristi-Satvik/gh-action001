# example.py

def hello_world():
    print("Hello, world!")  # This line is short enough

def long_line_example():
    # This line is intentionally long to test max-line-length
    print("This is a very long line that should trigger flake8 max-line-length if it's too long for the configured limit")
