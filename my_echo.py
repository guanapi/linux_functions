import sys

def my_echo(text):
    print(text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python my_echo.py <text>")
    else:
        my_echo(sys.argv[1])