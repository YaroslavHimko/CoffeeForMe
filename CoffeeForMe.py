from User import User as User
from utils import init_db, drop_db, fill_db


def main():
    init_db()
    fill_db()
    user = User()
    user.user_action()


if __name__ == "__main__":
    main()
