import sys

def cat(file):
    with open(file, 'r') as f:
        print(f.read(), end='')

if __name__ == "__main__":
    cat(sys.argv[1])
