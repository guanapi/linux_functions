import sys


def cat(text_file):
    with open(text_file, "r") as file:
        for line in file:
            print(line, end= " ")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cat(sys.argv[1])
