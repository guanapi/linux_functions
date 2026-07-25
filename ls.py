import sys
import os


def my_ls(directory):
    directories = (os.listdir(directory))
    for i in directories:
        print(i, end=" ")


if __name__ == "__main__":
    try:
        my_ls(sys.argv[1])
    except:
        actual_directory = os.getcwd()
        my_ls(actual_directory)