import sys
import argparse

def cat(file, show_ends):
    try:
        with open(file, 'r') as f:
            content = f.read()

            if show_ends:
                content = content.replace('\n', '$\n')

            print(content, end='')
    except:
        print(f'cat: {file}: No such file or directory')

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('-E', action='store_true')

    parser.add_argument('file')

    args= parser.parse_args()

    cat(args.file, args.E)
