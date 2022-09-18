#!/usr/bin/env python
import getpass as gp
from typing import Tuple

def get_credentials() -> Tuple[str, str]:
    username = input('Username:')
    try:
        password = gp.getpass();
        return username, password
    except (gp.GetPassWarning, EOFError) as e:
        raise e

def login():
    pass


def main():
    try:
        username, password = get_credentials()
        print(username)
        print(password)
    except Exception as e:
        raise e

if __name__ == "__main__":
    main()
