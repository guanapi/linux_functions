import os
import argparse
import fnmatch

def my_find(start_dir, pattern):
    for root, dirs, files in os.walk(start_dir):
        for filename in fnmatch.filter(files, pattern):
            print(os.path.join(root, filename))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find files in a directory tree.')
    parser.add_argument('start_dir', type=str, help='The directory to start searching from')
    parser.add_argument('name', type=str, help='The filename pattern to search for ')
    args = parser.parse_args()
    my_find(args.start_dir, args.name)