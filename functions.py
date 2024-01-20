import os

FILEPATH = "todos.txt"

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w'):
        pass


def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as f:
        f.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello World")
