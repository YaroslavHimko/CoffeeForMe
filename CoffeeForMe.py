from User import User as User
from Database_init import init_db


def main():
    init_db()
    user = User()
    user.check_role()


if __name__ == "__main__":
    main()
