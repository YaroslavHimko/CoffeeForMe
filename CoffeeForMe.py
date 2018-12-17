#!/usr/bin/env python3
from User import User as User
from utils import init_db


def main():
    init_db()
    user = User()
    user.user_action()


if __name__ == "__main__":
    main()
