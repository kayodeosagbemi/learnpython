print("Practicing try catch")


def read_file_lines(filename):
    """Read a file by iterating over it and return a list of lines.

    This is memory-friendlier than reading the whole file into memory at once
    when the caller can process lines incrementally. For this simple example
    we collect and return the lines so behavior remains compatible.
    """
    lines = []
    with open(filename, "r", encoding="utf-8") as fh:
        for line in fh:
            lines.append(line)
    return lines


try:
    data = read_file_lines("basics.py")
    print(f"The type of the data from the readlines() method is {type(data)}")
    print("The data is below:")
    print(data)
except FileNotFoundError as fe:
    print(f"The error is that file not found")
else:
    print("The else block runs after the try block only if the try block runs successfully")
finally:
    print("This runs ANYWAY in the finally block.")
