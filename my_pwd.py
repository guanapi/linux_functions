import os


def my_pwd():
    """Print the current working directory"""
    try:
        cwd = os.getcwd()
        print(cwd)
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    my_pwd()  