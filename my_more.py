import argparse

def my_more(filename):
    line_per_page = 25
    line_counter = 0
    with open(filename) as file:
        for line in file:
            print(line.rstrip())
            line_counter += 1

            if line_counter == line_per_page:
                input("--Press enter to continue reading--")
                line_counter = 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    my_more(args.file)