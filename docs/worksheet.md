# Python Lab Worksheet

## Part A

`mkdir python_lab` creates the project directory, and `cd python_lab` moves into it. `mkdir src tests docs` creates separate directories for source code, tests, and documentation. `touch src/main.py src/utils.py src/config.py` creates the Python files, while `echo "My Python Lab Project" > docs/README.md` writes one line to the README using output redirection. `tree /F` displays the directory tree and its files recursively.

Separating code into `src`, `tests`, and `docs` keeps responsibilities clear even in a small project. Source files stay focused on application behavior, tests can verify that behavior without cluttering the implementation, and documentation explains the project for future readers. This structure also makes the project easier to grow and navigate.

## Part B

`.gitignore` tells Git which files should not be tracked. `__pycache__/` ignores Python's compiled cache directories, `*.pyc` ignores compiled Python bytecode files, and `.env` ignores environment files that may contain local configuration or secrets. These patterns keep generated artifacts and sensitive local settings out of the repository.

The commit history records each saved version of the project, including its message, author, timestamp, and changed files. Reading it reveals how the project developed over time and makes it easier to understand or recover earlier work.

## Part C

`src/utils.py` contains the reusable functions:

```python

def square(n):
    return n ** 2


def is_even(n):
    return n % 2 == 0


def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
```

`src/main.py` imports those functions with `from utils import celsius_to_fahrenheit, is_even, square`. When Python runs `main.py` from the `src` directory, it searches that directory for `utils.py`, loads its function definitions, and makes the imported names available to the main program.

Example tests:

```text
$ python main.py
Enter a number: 2
Square: 4.0
The number is even.
Fahrenheit: 35.6

$ python main.py
Enter a number: 3
Square: 9.0
The number is odd.
Fahrenheit: 37.4

$ python main.py
Enter a number: -10
Square: 100.0
The number is even.
Fahrenheit: 14.0
```

## Part D

The local repository was connected to the supplied public GitHub repository and pushed to `main`. The `feature/add-greeting` branch adds `greet(name)` to `utils.py`, calls it from `main.py`, and is pushed for a pull request into `main`.
